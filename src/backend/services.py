import os
from src.rag.vector_store import VectorStore
from src.agents.resume_agent import ResumeAgent
from src.agents.interview_agent import InterviewAgent
from src.agents.learning_agent import LearningAgent

class CareerAIService:
    def __init__(self):
        """Inicializa e conecta todos os componentes do Career-AI (RAG + Agentes)."""
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        db_path = os.path.join(project_root, "chroma_db")
        
        # Cria a instância única do banco de dados vetorial
        self.vector_store = VectorStore(db_path=db_path)
        
        # Inicializa os agentes passando o banco vetorial compartilhado
        self.resume_agent = ResumeAgent(self.vector_store)
        self.interview_agent = InterviewAgent(self.vector_store)
        self.learning_agent = LearningAgent(self.vector_store)

    def analyze_resume(self, name: str, role: str) -> str:
        """Serviço para acionar o ResumeAgent."""
        return self.resume_agent.analyze_resume(name, role)

    def get_interview_question(self, topic: str) -> dict:
        """Serviço para obter uma pergunta do InterviewAgent."""
        return self.interview_agent.get_question(topic)

    def evaluate_interview_response(self, question: str, answer: str, expected: str) -> str:
        """Serviço para avaliar a resposta com o InterviewAgent."""
        return self.interview_agent.evaluate_response(question, answer, expected)

    def generate_roadmap(self, topic: str) -> str:
        """Serviço para gerar roteiros com o LearningAgent."""
        return self.learning_agent.generate_roadmap(topic)

# Instância Singleton global do serviço para ser injetada nas rotas
career_service = CareerAIService()
