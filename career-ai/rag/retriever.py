from .vector_store import VectorStore

class ContextRetriever:
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store
        
    def get_relevant_context(self, user_query: str) -> str:
        """
        Dada a pergunta do usuário, gera o embedding da query e 
        busca no banco vetorial o contexto para o LLM responder.
        """
        # TODO: Chamar API de Embedding para converter user_query em um vetor
        dummy_query_embedding = [0.1, 0.2, 0.3]
        
        # Realiza a busca semântica no banco
        results = self.vector_store.search(dummy_query_embedding, top_k=2)
        
        # Formata os resultados em uma string de contexto única
        context = "\n---\n".join([str(doc) for doc in results])
        return context
