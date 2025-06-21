import chromadb
from chromadb.utils import embedding_functions

client = chromadb.Client()
collection = client.get_or_create_collection(name="book_versions")

def store_version(text, version, role, embedding):
    collection.add(
        documents=[text],
        metadatas=[{"version": version, "role": role}],
        ids=[f"{role}_v{version}"],
        embeddings=[embedding]
    )

def search_version(query_embedding, top_k=1):
    return collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
