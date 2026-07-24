from fastapi import FastAPI
...
   try:
    from rag import get_context
except Exception as e:
    print("RAG disabled:", e)

    def get_context(question):
        return None
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from database import initialize_database
from services.policy_service import generate_policy

from services.llm_service import ask_llm

app = FastAPI(title="ITGenie Enterprise")
initialize_database()

# -------------------------------------------------
# Static Files
# -------------------------------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# -------------------------------------------------
# Templates
# -------------------------------------------------
templates = Jinja2Templates(directory="templates")

# -------------------------------------------------
# Request Models
# -------------------------------------------------
class QuestionRequest(BaseModel):
    question: str


class PolicyRequest(BaseModel):
    policy_name: str
    policy_type: str
    purpose: str


# -------------------------------------------------
# Dashboard
# -------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
    )


# -------------------------------------------------
# AI Assistant
# -------------------------------------------------
@app.get("/assistant", response_class=HTMLResponse)
async def assistant(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="assistant.html",
    )


# -------------------------------------------------
# Policy Management
# -------------------------------------------------
@app.get("/policy", response_class=HTMLResponse)
async def policy(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="policy.html",
    )


# -------------------------------------------------
# Risk Management
# -------------------------------------------------
@app.get("/risk", response_class=HTMLResponse)
async def risk(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="risk.html",
    )


# -------------------------------------------------
# Compliance
# -------------------------------------------------
@app.get("/compliance", response_class=HTMLResponse)
async def compliance(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="compliance.html",
    )


# -------------------------------------------------
# Internal Audit
# -------------------------------------------------
@app.get("/audit", response_class=HTMLResponse)
async def audit(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="audit.html",
    )


# -------------------------------------------------
# Health Check
# -------------------------------------------------
@app.get("/health")
def health():
    return {
        "status": "Running",
        "application": "ITGenie Enterprise",
        "llm": "Ollama Llama 3.1"
    }


# -------------------------------------------------
# Ask AI Assistant
# -------------------------------------------------
@app.post("/ask")
def ask(req: QuestionRequest):

    context = get_context(req.question)

    if context is None:
        return {
            "question": req.question,
            "answer": "I couldn't find this information in the ITGenie knowledge base.",
            "source": "Knowledge Base"
        }

    answer = ask_llm(req.question, context)

    return {
        "question": req.question,
        "answer": answer,
        "source": "ITGenie Knowledge Base"
    }

# -------------------------------------------------
# Generate Policy
# -------------------------------------------------
@app.post("/generate-policy")
def generate_policy_api(req: PolicyRequest):

    policy = generate_policy(
        req.policy_name,
        req.policy_type,
        req.purpose
    )

    return {
        "policy": policy
    }
