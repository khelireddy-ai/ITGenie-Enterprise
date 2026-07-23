import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"


def ask_llm(question, context):

    prompt = f"""
You are ITGenie Enterprise AI Assistant.

You MUST answer ONLY using the Context below.

=================================================
CONTEXT
=================================================

{context}

=================================================
QUESTION
=================================================

{question}

STRICT RULES

1. Answer ONLY from the Context.
2. NEVER use your own knowledge.
3. NEVER guess.
4. NEVER assume.
5. NEVER create policy values.
6. NEVER create numbers.
7. NEVER invent leave limits, passwords, dates, or procedures.
8. Every sentence in your answer MUST exist in the Context.
9. If the Context does NOT explicitly contain the answer, reply EXACTLY:

I couldn't find this information in the ITGenie knowledge base.

OUTPUT FORMAT

### Short Answer
(Maximum 2 lines)

### Key Points
- Point 1
- Point 2
- Point 3
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "top_p": 0.1,
            "top_k": 10,
            "num_predict": 120
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    return data.get("response", "No response received.")
