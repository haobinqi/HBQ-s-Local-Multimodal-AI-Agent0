from modules.text_embedder import embed_text
from modules.vector_store import paper_collection, image_collection
from modules.clip_embedder import embed_text_for_clip

# 搜索论文
def search_paper(query, top_k=5):
    emb = embed_text(query)  # 384维
    res = paper_collection.query(
        query_embeddings=[emb],
        n_results=top_k
    )

    results = []
    for meta in res["metadatas"][0]:
        results.append({
            "path": meta["path"],
            "page": meta["page"],
            "category": meta.get("category", "")
        })
    return results

# 搜索图片
def search_image(
    query,
    top_k=10,
    distance_threshold=0.25  # 归一化后的阈值
):
    emb = embed_text_for_clip(query)

    res = image_collection.query(
        query_embeddings=[emb],
        n_results=top_k,
        include=["metadatas", "distances"]
    )

    results = []

    metadatas = res.get("metadatas", [[]])[0]
    distances = res.get("distances", [[]])[0]

    if not distances:  # 没有返回
        return results

    # 归一化到 0~1
    min_dist = min(distances)
    max_dist = max(distances)
    range_dist = max_dist - min_dist if max_dist != min_dist else 1.0

    for meta, dist in zip(metadatas, distances):
        normalized = (dist - min_dist) / range_dist
        if normalized <= distance_threshold:
            results.append({
                "path": meta["path"],
                "distance": float(normalized)
            })

    return results
