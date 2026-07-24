import requests

OLLAMA_URL = "http://20.235.243.2:11434/api/generate"
MODEL = "llama3.2:3b"


def ask_llm(question, context=""):

    prompt = f"""
You are ITGenie Enterprise AI Assistant.

Answer only using the context below.

Context:
{context}

Question:
{question}

If the context is empty, answer using your general ISMS knowledge.

Keep the answer concise and professional.
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        return response.json()["response"].strip()

    except Exception:
        return """
✅ ITGenie Enterprise is successfully deployed on Azure.

⚠ AI service is currently unavailable because Ollama is running locally.

Next step:
- Deploy Ollama on an Azure Virtual Machine
OR
- Configure Azure OpenAI.
"""
