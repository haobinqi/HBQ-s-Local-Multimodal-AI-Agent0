import os
import uuid
from modules.clip_embedder import embed_image
from modules.vector_store import image_collection

def add_image(image_path):
    emb = embed_image(image_path)
    image_collection.add(
        documents=[image_path],
        embeddings=[emb],
        metadatas=[{"path": image_path}],
        ids=[str(uuid.uuid4())]
    )
    print(f"已添加图片: {image_path}")

def batch_index_images(folder):
    for f in os.listdir(folder):
        if f.lower().endswith((".jpg", ".png", ".jpeg")):
            add_image(os.path.join(folder, f))
