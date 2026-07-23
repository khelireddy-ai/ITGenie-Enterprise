from pathlib import Path
from docx import Document

# ----------------------------------------
# Project Paths
# ----------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

POLICIES_DIR = PROJECT_ROOT / "Policies"

EXTRACTED_DIR = PROJECT_ROOT / "Knowledge" / "Extracted"

EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)


# ----------------------------------------
# Read Word Document
# ----------------------------------------

def extract_docx(docx_path):
    """
    Extract text from a Word document.
    """

    document = Document(docx_path)

    text = ""

    for para in document.paragraphs:
        if para.text.strip():
            text += para.text + "\n"

    return text


# ----------------------------------------
# Process All Word Documents
# ----------------------------------------

def process_documents():

    docx_files = list(POLICIES_DIR.glob("*.docx"))

    if not docx_files:
        print("No Word documents found.")
        return

    print(f"Found {len(docx_files)} Word document(s)\n")

    for docx in docx_files:

        print(f"Reading : {docx.name}")

        text = extract_docx(docx)

        output_file = EXTRACTED_DIR / f"{docx.stem}.txt"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(text)

        print(f"Saved   : {output_file.name}\n")

    print("✅ Document extraction completed successfully.")


# ----------------------------------------
# Main
# ----------------------------------------

if __name__ == "__main__":
    process_documents()