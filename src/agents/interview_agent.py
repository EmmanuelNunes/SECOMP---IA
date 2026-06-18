import os
from src.rag.vector_store import VectorStore
from src.rag.retriever import ContextRetriever

class InterviewAgent:
    def __init__(self, vector_store: VectorStore):
        """Inicializa o Agente de Entrevistas Simuladas."""
        self.vector_store = vector_store
        self.retriever = ContextRetriever(vector_store)

    def get_question(self, topic: str = "RAG") -> dict:
        """
        Busca uma pergunta de entrevista relevante sobre o tópico no banco de dados vetorial.
        """
        # Faz uma busca por similaridade semântica para encontrar uma pergunta adequada
        query = f"Pergunta para simulação de entrevista técnica sobre: {topic}"
        results = self.vector_store.search(query, top_k=1)
        
        if not results:
            return {
                "question": f"Explique o funcionamento básico de um sistema baseado em {topic}.",
                "expected_answer": "Resposta teórica padrão baseada na documentação da tecnologia."
            }
            
        content = results[0]["content"]
        # Extrai os dados se o formato for o gerado no ingestion:
        # Pergunta para simulação de entrevista técnica: '...'. Resposta sugerida esperada: ...
        q_text = "Pergunta sobre " + topic
        ans_text = "Resposta conceitual."
        
        if "Pergunta para simulação de entrevista técnica: '" in content:
            parts = content.split("Pergunta para simulação de entrevista técnica: '")
            subparts = parts[1].split("'. Resposta sugerida esperada: ")
            q_text = subparts[0]
            ans_text = subparts[1]
        else:
            q_text = content
            
        return {
            "question": q_text,
            "expected_answer": ans_text
        }

    def evaluate_response(self, question: str, user_answer: str, expected_answer: str) -> str:
        """
        Compara a resposta do usuário com a resposta de referência e gera um feedback estruturado.
        """
        # Se a chave da API estiver no ambiente, podemos usar um modelo real.
        api_key_present = os.getenv("OPENAI_API_KEY") or os.getenv("GEMINI_API_KEY")
        
        if api_key_present:
            # Implementação real com LLM pode ser adicionada aqui (Ex: LangChain ChatOpenAI/Gemini)
            pass

        # Lógica heurística rica de feedback
        # Calcula aderência semântica simples
        words_user = set(user_answer.lower().split())
        words_expected = set(expected_answer.lower().split())
        intersection = words_user.intersection(words_expected)
        
        score = min(100, int((len(intersection) / max(1, len(words_expected))) * 200)) # Heurística simples
        if score > 80:
            level = "Excelente"
            verdict = "Sua resposta cobre perfeitamente todos os conceitos técnicos fundamentais e demonstra domínio do tema."
        elif score > 40:
            level = "Regular"
            verdict = "Você mencionou pontos importantes, mas pode enriquecer sua explicação com mais detalhes arquiteturais."
        else:
            level = "Insuficiente"
            verdict = "Sua resposta foi muito breve ou desviou-se do conceito principal esperado. Recomendamos revisar o material téorico."

        feedback = f"""### 📝 Avaliação da Resposta da Entrevista
* **Pergunta:** {question}
* **Sua Resposta:** *"{user_answer}"*

---

#### 📊 Desempenho e Pontuação
* **Pontuação Estimada:** {score}/100
* **Nível:** {level}

#### 💡 Feedback Detalhado
{verdict}

#### 🔑 Resposta Esperada de Referência
> {expected_answer}
"""
        return feedback
