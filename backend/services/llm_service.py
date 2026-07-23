import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"


def ask_llm(question, context):
    return """
✅ ITGenie is successfully deployed on Azure.

⚠ AI service is currently unavailable because Ollama is running locally.

Next step:
- Deploy Ollama on Azure VM
OR
- Configure Azure OpenAI.
"""
