from .vector_store import VectorStore

class ContextRetriever:
    def __init__(self, vector_store: VectorStore):
        """Inicializa o buscador com uma instância do VectorStore."""
        self.vector_store = vector_store
        
    def get_relevant_context(self, user_query: str, top_k: int = 2) -> str:
        """
        Dada a consulta do usuário, realiza busca semântica no banco vetorial
        e formata os resultados em um único bloco de texto que servirá de
        contexto enriquecido para o LLM.
        """
        results = self.vector_store.search(user_query, top_k=top_k)
        
        # Une o conteúdo textual dos documentos mais similares encontrados
        context_parts = []
        for res in results:
            content = res["content"]
            meta = res["metadata"]
            meta_str = f"[{meta.get('type', 'desconhecido').upper()}]"
            context_parts.append(f"{meta_str} {content}")
            
        context = "\n---\n".join(context_parts)
        return context
