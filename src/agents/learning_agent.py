import os
from src.rag.vector_store import VectorStore
from src.rag.retriever import ContextRetriever

class LearningAgent:
    def __init__(self, vector_store: VectorStore):
        """Inicializa o Agente de Planos de Estudo."""
        self.vector_store = vector_store
        self.retriever = ContextRetriever(vector_store)

    def generate_roadmap(self, topic: str) -> str:
        """
        Gera um plano de estudo estruturado (roadmap) com base no tópico requisitado
        e nos dados recuperados do ChromaDB.
        """
        # 1. Recupera contexto de roteiros de estudo (study guides) no banco vetorial
        query = f"Tópico de Estudo: {topic}"
        context = self.retriever.get_relevant_context(query, top_k=1)
        
        if not context:
            # Fallback se o RAG não retornar nada específico
            context = f"[STUDY_GUIDE] Tópico de Estudo: {topic}. Resumo da tecnologia: Introdução geral a conceitos de desenvolvimento de software."

        # 2. Gera o Roadmap em Markdown
        # Se a chave da API estiver no ambiente, podemos usar um modelo real.
        api_key_present = os.getenv("OPENAI_API_KEY") or os.getenv("GEMINI_API_KEY")
        
        if api_key_present:
            # Integração real com LLM pode ser adicionada aqui (Ex: LangChain ChatOpenAI/Gemini)
            pass

        # Geração rica formatada
        roadmap = f"""### 🗺️ Roteiro de Aprendizado Customizado - Career-AI
* **Tópico Central:** {topic}

---

#### 📖 Visão Geral (RAG Context)
{context}

#### 📅 Cronograma de Estudo Recomendado

* **Dia 1: Fundamentos Básicos**
  * Entenda a definição e a teoria inicial por trás de **{topic}**.
  * Atividade: Leitura de artigos e documentações oficiais da tecnologia.

* **Dia 2: Prática e Setup**
  * Configure o ambiente local de desenvolvimento e crie o seu primeiro "Hello World" ou script básico.
  * Atividade: Executar os laboratórios práticos do repositório da SECOMP.

* **Dia 3: Conceitos Avançados**
  * Aprofunde-se nos subtemas, integrações, APIs e boas práticas de arquitetura.
  * Atividade: Desenvolver um pequeno MVP ou caso de uso prático.

#### 🛠️ Exercício de Fixação
* Crie um projeto pessoal unindo **{topic}** com integração de dados e documente-o usando práticas de Engenharia de Prompt no README.
"""
        return roadmap
