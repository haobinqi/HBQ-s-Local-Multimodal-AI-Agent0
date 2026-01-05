# 本地 AI 智能文献与图像管理助手 (Local Multimodal AI Agent)

## 1. 项目简介 (Project Introduction)
本项目实现了一个 本地运行的多模态 AI Agent，支持对论文（PDF）和图片数据进行统一的向量化表示、存储与语义检索。系统融合了 Sentence-BERT、CLIP 与 ChromaDB，并通过 Streamlit 提供可视化交互界面。

主要功能包括：

1. 论文自动解析与语义分类
2. 论文语义搜索（Semantic Search）
3. 图像向量化与索引
4. 以文搜图（Text-to-Image Retrieval）
5. 本地向量数据库持久化存储

## 2. 核心技术

| 模块        | 技术                                     |
| --------- | -------------------------------------- |
| 文本向量化     | SentenceTransformer (all-MiniLM-L6-v2) |
| 图像 / 文本对齐 | CLIP (ViT-B/32)                        |
| 向量数据库     | ChromaDB                               |
| PDF 解析    | PyMuPDF                                |
| 可视化界面     | Streamlit                              |


## 3. 项目结构

```bash
local_multimodal_ai_agent/
│
├── app.py                  # Streamlit 可视化界面
├── main.py                 # 命令行入口
├── requirements.txt
├── README.md
│
├── data/
│   ├── papers_raw/         # 原始 PDF
│   ├── papers_organized/   # 分类后的论文
│   └── images/             # 原始图片
│
├── vector_db/
│   └── chroma/             # ChromaDB 向量数据库（持久化）
│
└── modules/
    ├── paper_manager.py    # 论文解析与分类
    ├── image_manager.py    # 图像索引
    ├── text_embedder.py    # Sentence-BERT
    ├── clip_embedder.py    # CLIP 编码
    ├── search.py           # 语义搜索逻辑
    └── vector_store.py     # ChromaDB 封装
 

```

## 4. 环境配置

### 4.1 创建虚拟环境

```bash
conda create -n clip_lab python=3.9
conda activate clip_lab
```

### 4.2 安装依赖

```bash
pip install -r requirements.txt
```
首次运行会自动下载 SentenceTransformer 和 CLIP 模型，请确保网络通畅。


## 5. 使用方式

### 5.1 命令行运行
*   **添加并分类论文**: 
```bash
python main.py add_paper data/papers_raw/example.pdf --topics NLP,CV,RL
```
*   功能：
    *   自动解析 PDF
    *   语义分类
    *   写入向量数据库

*   **批量整理论文**: 
```bash
python main.py organize_papers data/papers_raw --topics NLP,CV,RL
```
*   实现整理指定文件夹中的所有论文。

*   **语义搜索论文**: 
```bash
python main.py search_paper "Transformer attention mechanism"
```
*   返回内容包括：
    *   文件路径
    *   页码
    *   分类标签

*   **图像索引**: 
```bash
python main.py index_images data/images
```
*   搜索图片前需运行该命令将图片添加到数据库。

*   **以文搜图**: 
```bash
python main.py search_image "panda"
``` 
*   系统会返回与文本语义最接近的图片路径。



### 5.2 可视化界面
*   **启动Web界面**: 
```bash
streamlit run app.py
``` 
*   界面支持：
    *   论文上传与分类
    *   批量整理论文
    *   论文语义搜索（结果可视化）
    *   图像索引
    *   以文搜图（图片直接展示）

### 5.3 清空向量数据库（可选）
*   如需重置索引，可直接删除：
```bash
vector_db/chroma/
``` 
## 6. github链接和运行截图
### 6.1 github链接
*   https://github.com/haobinqi/HBQ-s-Local-Multimodal-AI-Agent0

### 6.2 运行截图
*   result文件夹下

### 6.3 运行视频
*   

