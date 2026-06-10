# Laboratório 05: RAG + ChromaDB

## Objetivo
Criar o primeiro sistema RAG (Retrieval-Augmented Generation).

## Instalação
Garanta que a dependência do banco vetorial local está instalada:
```bash
pip install chromadb
```

## Criar Coleção
Instanciamos o cliente e criamos a nossa "tabela" vetorial.
```python
import chromadb
client = chromadb.Client()
collection = client.create_collection("secomp")
```

## Inserir Documento
Inserimos textos reais no banco. Em um fluxo normal, o Chroma calcula os embeddings por debaixo dos panos automaticamente (usando um modelo padrão).
```python
collection.add(
    documents=["RAG significa Retrieval Augmented Generation"],
    ids=["doc1"]
)
```

## Consulta
Fazemos a busca baseada no significado da frase.
```python
results = collection.query(
    query_texts=["O que é RAG?"]
)
print(results)
```
