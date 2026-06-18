from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .services import career_service

router = APIRouter(prefix="/api")

# --- Esquemas Pydantic para Validação ---
class ResumeRequest(BaseModel):
    name: str
    role: str

class InterviewEvaluateRequest(BaseModel):
    question: str
    user_answer: str
    expected_answer: str

# --- Endpoints da API ---

@router.post("/resume/analyze")
def analyze_resume_endpoint(req: ResumeRequest):
    """Analisa o currículo de um candidato indexado no banco vetorial."""
    try:
        analysis = career_service.analyze_resume(req.name, req.role)
        return {"analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/interview/question")
def get_interview_question_endpoint(topic: str = "RAG"):
    """Gera uma pergunta técnica baseada no tópico."""
    try:
        question_data = career_service.get_interview_question(topic)
        return question_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/interview/evaluate")
def evaluate_interview_endpoint(req: InterviewEvaluateRequest):
    """Avalia a resposta dada pelo candidato à pergunta de entrevista."""
    try:
        feedback = career_service.evaluate_interview_response(
            req.question, req.user_answer, req.expected_answer
        )
        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/learning/roadmap")
def generate_roadmap_endpoint(topic: str):
    """Gera um plano de estudos personalizado para um tema técnico."""
    try:
        roadmap = career_service.generate_roadmap(topic)
        return {"roadmap": roadmap}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
