import streamlit as st
import os

from modules.paper_manager import add_paper, batch_organize
from modules.search import search_paper, search_image
from modules.image_manager import batch_index_images

# 页面配置
st.set_page_config(
    page_title="Local Multimodal AI Agent",
    layout="wide"
)

st.title("Welcome to HBQ's Local Multimodal AI Agent")

tabs = st.tabs([
    "添加 / 分类论文",
    "批量整理论文",
    "语义搜索论文",
    "图像索引",
    "以文搜图"
])

# 添加 / 分类论文
with tabs[0]:
    st.header("添加并自动分类论文")

    uploaded_file = st.file_uploader("上传 PDF 文件", type=["pdf"])
    topics = st.text_input("输入主题（用逗号分隔，如 NLP,CV,RL）")

    if uploaded_file is not None:
        save_dir = "data/papers_raw"
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, uploaded_file.name)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())

        if st.button("开始分析并分类"):
            with st.spinner("正在分类，请稍候..."):
                add_paper(save_path, topics)
            st.success("论文已成功添加并分类")

# 批量整理论文
with tabs[1]:
    st.header("批量整理论文文件夹")

    folder = st.text_input(
        "输入论文文件夹路径",
        value="data/papers_raw"
    )
    topics = st.text_input(
        "主题（如 NLP,CV,RL）",
        key="batch_topics"
    )

    if st.button("一键整理"):
        with st.spinner("正在整理，请稍候..."):
            batch_organize(folder, topics)
        st.success("批量整理完成")


# 语义搜索论文
with tabs[2]:
    st.header("语义搜索论文")

    query = st.text_input("输入查询问题，例如：transformer attention")

    if st.button("搜索论文"):
        results = search_paper(query)

        if not results:
            st.warning("未找到相关论文")
        else:
            st.success(f"共找到 {len(results)} 条结果")

            for r in results:
                st.markdown(f"""
                **文件路径**  
                `{r['path']}`  

                **页码**：{r['page']}  
                **分类**：{r['category']}  
                ---
                """)


# 图像索引
with tabs[3]:
    st.header("图像文件夹索引")

    img_folder = st.text_input(
        "输入图像文件夹路径",
        value="data/images"
    )

    if st.button("开始索引"):
        with st.spinner("正在索引图片，请稍候..."):
            batch_index_images(img_folder)
        st.success("图像索引完成")

# 以文搜图
with tabs[4]:
    st.header("以文搜图（Text → Image）")

    img_query = st.text_input("输入图像描述，例如：panda")

    if st.button("搜索图片"):
        results = search_image(img_query)

        if not results:
            st.warning("未找到匹配图片")
        else:

            for r in results:
                print(r)

            st.success(f"共找到 {len(results)} 张图片")

            cols = st.columns(2)

            for i, img_info in enumerate(results):
                img_path = img_info["path"]
                if os.path.exists(img_path):
                    cols[i % 2].image(
                        img_path,
                        use_container_width=True
                    )
                else:
                    cols[i % 2].error(f"文件不存在：{img_path}")
