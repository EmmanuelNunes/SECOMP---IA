import chromadb
import os
from .embeddings import EmbeddingModel

class VectorStore:
    def __init__(self, db_path="chroma_db"):
        """Inicializa a conexão persistente com o ChromaDB."""
        # Se db_path for relativo, resolvemos a partir da raiz do projeto
        if not os.path.isabs(db_path):
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            db_path = os.path.join(project_root, db_path)
            
        self.client = chromadb.PersistentClient(path=db_path)
        self.embedding_model = EmbeddingModel()
        self.collection = self.client.get_or_create_collection(name="secomp_career_ai")

    def add_documents(self, docs, metadatas=None, ids=None):
        """Vetoriza e adiciona documentos ao ChromaDB."""
        if not docs:
            return
            
        if ids is None:
            ids = [f"doc_{i}" for i in range(len(docs))]
            
        if metadatas is None:
            metadatas = [{} for _ in docs]

        # Calcula os embeddings locais
        embeddings = [self.embedding_model.get_embedding(doc) for doc in docs]
        
        self.collection.add(
            documents=docs,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        print(f"{len(docs)} documentos adicionados/atualizados no banco vetorial.")

    def search(self, query_text, top_k=3):
        """Busca semântica por similaridade dos embeddings."""
        query_embedding = self.embedding_model.get_embedding(query_text)
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        ids = results.get("ids", [[]])[0]
        distances = results.get("distances", [[]])[0]
        
        formatted_results = []
        for i, doc, meta, dist in zip(ids, documents, metadatas, distances):
            formatted_results.append({
                "id": i,
                "content": doc,
                "metadata": meta,
                "distance": dist
            })
            
        return formatted_results
