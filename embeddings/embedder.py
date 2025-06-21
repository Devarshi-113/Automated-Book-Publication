from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # Small and fast; good enough for versioning

def get_embedding(text: str):
    return model.encode(text).tolist()  # Convert NumPy array to list for ChromaDB
