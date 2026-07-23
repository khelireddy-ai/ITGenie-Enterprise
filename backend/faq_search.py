import pandas as pd
from sentence_transformers import SentenceTransformer
from pathlib import Path

# ---------------------------------------
# Paths
# ---------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

EXCEL_FILE = PROJECT_ROOT / "Master" / "ITGenie_Knowledge_Master.xlsx"

# ---------------------------------------
# Load Model
# ---------------------------------------

print("Loading FAQ Search Engine...")

model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------------------------------
# Load Excel
# ---------------------------------------

df = pd.read_excel(EXCEL_FILE)

questions = df["Employee Question"].fillna("").tolist()
answers = df["Approved Answer"].fillna("").tolist()
sources = df["Source Policy"].fillna("").tolist()
print(f"Loaded {len(questions)} FAQs")

# ---------------------------------------
# Create Embeddings
# ---------------------------------------

question_embeddings = model.encode(questions)

# ---------------------------------------
# Search
# ---------------------------------------

while True:

    print("\n==============================")

    user_question = input("Ask ITGenie (type exit): ")

    if user_question.lower() == "exit":
        break

    user_embedding = model.encode(user_question)

    scores = model.similarity(user_embedding, question_embeddings)

    best_index = scores.argmax()

    print("\nBest Match\n")

    print("Question :", questions[best_index])

    print("\nAnswer :")

    print(answers[best_index])

    print("\nSource :", sources[best_index])