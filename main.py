import argparse
from modules.paper_manager import add_paper, batch_organize
from modules.search import search_paper, search_image
from modules.image_manager import batch_index_images

def main():
    parser = argparse.ArgumentParser("Local Multimodal AI Agent")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("add_paper")
    p1.add_argument("path")
    p1.add_argument("--topics", default="")

    p2 = sub.add_parser("organize_papers")
    p2.add_argument("folder")
    p2.add_argument("--topics", default="")

    p3 = sub.add_parser("search_paper")
    p3.add_argument("query")

    p4 = sub.add_parser("index_images")
    p4.add_argument("folder")

    p5 = sub.add_parser("search_image")
    p5.add_argument("query")

    args = parser.parse_args()

    # 添加 / 分类论文
    if args.cmd == "add_paper":
        add_paper(args.path, args.topics)

    # 批量整理论文
    elif args.cmd == "organize_papers":
        batch_organize(args.folder, args.topics)

    # 语义搜索论文
    elif args.cmd == "search_paper":

        results = search_paper(args.query)

        if results:

            for r in results:
                print(f"{r['path']} | page: {r['page']} | category: {r['category']}")

        else:

            print(f"No results found for query: {args.query}")

    # 图像索引
    elif args.cmd == "index_images":
        batch_index_images(args.folder)

    # 以文搜图
    elif args.cmd == "search_image":

        results = search_image(args.query)

        if results:

            for r in results:
                print(r)

        else:

            print(f"No results found for query: {args.query}")

if __name__ == "__main__":
    main()
