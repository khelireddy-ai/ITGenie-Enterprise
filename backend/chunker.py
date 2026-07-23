import json
from pathlib import Path

# ----------------------------------------
# Project Paths
# ----------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

EXTRACTED_DIR = PROJECT_ROOT / "Knowledge" / "Extracted"
CHUNKS_DIR = PROJECT_ROOT / "Knowledge" / "Chunks"

CHUNKS_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------------------
# Chunk Settings
# ----------------------------------------

CHUNK_SIZE = 500      # words per chunk
OVERLAP = 50          # overlap between chunks

# ----------------------------------------
# Create Chunks
# ----------------------------------------

def create_chunks(text):

    words = text.split()

    chunks = []

    start = 0
    chunk_id = 1

    while start < len(words):

        end = start + CHUNK_SIZE

        chunk_text = " ".join(words[start:end])

        chunks.append({
            "chunk_id": chunk_id,
            "text": chunk_text
        })

        chunk_id += 1

        start += CHUNK_SIZE - OVERLAP

    return chunks

# ----------------------------------------
# Process All TXT Files
# ----------------------------------------

def process_documents():

    txt_files = list(EXTRACTED_DIR.glob("*.txt"))

    if not txt_files:
        print("No extracted text files found.")
        return

    for txt_file in txt_files:

        print(f"Reading : {txt_file.name}")

        with open(txt_file, "r", encoding="utf-8") as file:
            text = file.read()

        chunks = create_chunks(text)

        for chunk in chunks:
            chunk["document"] = txt_file.stem

        output_file = CHUNKS_DIR / f"{txt_file.stem}_chunks.json"

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(chunks, file, indent=4)

        print(f"Saved : {output_file.name}")
        print(f"Chunks : {len(chunks)}\n")

    print("✅ Chunking Completed Successfully.")

# ----------------------------------------
# Main
# ----------------------------------------

if __name__ == "__main__":
    process_documents()