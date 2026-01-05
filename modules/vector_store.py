import chromadb
from chromadb.config import Settings

# 使用 PersistentClient，保证写入磁盘持久化
client = chromadb.PersistentClient(
    path="vector_db/chroma",  # 数据库存储路径
    settings=Settings(anonymized_telemetry=False)
)

# 创建或获取论文集合（384维）
paper_collection = client.get_or_create_collection(
    name="papers",
    metadata={"description": "Collection for storing paper embeddings"}
)

# 创建或获取图片集合（512维）
image_collection = client.get_or_create_collection(
    name="images",
    metadata={"description": "Collection for storing image embeddings"}
)

def persist_collections():
    paper_collection.persist()
    image_collection.persist()
