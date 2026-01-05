import os
import shutil
import uuid
from modules.pdf_parser import parse_pdf_by_page
from modules.text_embedder import embed_text
from modules.vector_store import paper_collection

def classify_paper(text, topics):
    if not topics:
        return "Uncategorized"
    topic_list = [t.strip() for t in topics.split(",")]
    text_emb = embed_text(text)
    sims = []
    for t in topic_list:
        sims.append((t, embed_text(t) @ text_emb))
    return max(sims, key=lambda x: x[1])[0]

def add_paper(pdf_path, topics=""):
    pages = parse_pdf_by_page(pdf_path)
    full_text = " ".join([p["text"] for p in pages])

    category = classify_paper(full_text[:1000], topics)

    target_dir = os.path.join("data/papers_organized", category)
    os.makedirs(target_dir, exist_ok=True)

    new_path = os.path.join(target_dir, os.path.basename(pdf_path))
    shutil.copy(pdf_path, new_path)

    for p in pages:
        emb = embed_text(p["text"])
        paper_collection.add(
            documents=[p["text"]],
            embeddings=[emb],
            metadatas=[{
                "path": new_path,
                "page": p["page"],
                "category": category
            }],
            ids=[str(uuid.uuid4())]
        )

    print(f"已添加论文: {new_path} | 分类: {category}")

def batch_organize(folder, topics):
    for f in os.listdir(folder):
        if f.endswith(".pdf"):
            add_paper(os.path.join(folder, f), topics)
