# Exemplo de Vector Store simulada (ou usando ChromaDB/FAISS/Qdrant no futuro)

class VectorStore:
    def __init__(self):
        self.documents = []
        self.embeddings = []
        
    def add_documents(self, docs):
        """Adiciona documentos ao banco de dados vetorial."""
        self.documents.extend(docs)
        # TODO: Chamar API de Embeddings (ex: text-embedding-3-small) 
        # para transformar os docs em vetores e salvar em self.embeddings
        print(f"{len(docs)} documentos indexados com sucesso no Vector Store.")

    def search(self, query_embedding, top_k=3):
        """Busca os documentos mais similares baseados no embedding da query."""
        # TODO: Implementar busca de similaridade do cosseno real
        print(f"Buscando os {top_k} documentos mais relevantes...")
        
        # Retorno dummy (apenas para estruturação inicial)
        return self.documents[:top_k]
