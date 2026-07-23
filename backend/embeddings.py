import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb

# ------------------------------------
# Paths
# ------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CHUNKS_DIR = PROJECT_ROOT / "Knowledge" / "Chunks"

# ------------------------------------
# Load Embedding Model
# ------------------------------------

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

# ------------------------------------
# ChromaDB
# ------------------------------------

client = chromadb.PersistentClient(path=str(PROJECT_ROOT / "Embeddings"))

collection = client.get_or_create_collection("ITGenie")

# ------------------------------------
# Read Chunk Files
# ------------------------------------

json_files = list(CHUNKS_DIR.glob("*_chunks.json"))

for json_file in json_files:

    print(f"Processing {json_file.name}")

    with open(json_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    for chunk in chunks:

        embedding = model.encode(chunk["text"]).tolist()

        collection.add(
            ids=[f"{chunk['document']}_{chunk['chunk_id']}"],
            embeddings=[embedding],
            documents=[chunk["text"]],
            metadatas=[{
                "document": chunk["document"],
                "chunk": chunk["chunk_id"]
            }]
        )

print("\n✅ Embeddings Created Successfully!")