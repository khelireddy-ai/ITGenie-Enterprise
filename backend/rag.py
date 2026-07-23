from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
EMBEDDING_DIR = PROJECT_ROOT / "Embeddings"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=str(EMBEDDING_DIR))
collection = client.get_collection("ITGenie")


def get_context(question):

    embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3,
        include=["documents", "metadatas", "distances"]
    )

    documents = results["documents"][0]
    distances = results["distances"][0]

    if not documents:
        return None

    # Reject weak matches
    if distances[0] > 1.2:
        return None

    context = "\n\n".join(documents)

    return context
