from services.llm_service import ask_llm

context = """
Secure coding is the practice of developing software
that protects against vulnerabilities.
"""

question = "What is secure coding?"

print(ask_llm(question, context))
