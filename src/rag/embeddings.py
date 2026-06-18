from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """Inicializa o modelo local de embeddings usando SentenceTransformers."""
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, text: str):
        """Gera o embedding vetorial de um texto."""
        return self.model.encode(text).tolist()
