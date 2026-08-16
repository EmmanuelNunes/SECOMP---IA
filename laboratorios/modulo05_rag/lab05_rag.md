# Laboratório 05: RAG + ChromaDB & Paradigmas de Contexto

## 🎯 Objetivo
1. Compreender quando aplicar **RAG** vs. **CAG** vs. **MAG** em projetos práticos de IA.
2. Criar e operar seu primeiro banco vetorial local com **ChromaDB**.
3. Realizar ingestão de documentos, cálculo de embeddings automáticos e busca por similaridade semântica (cosseno).

---

## 💡 Panorama Conceitual: RAG vs. CAG vs. MAG

Antes de rodar o código, entenda onde o ChromaDB e o RAG se encaixam:
* **🔍 RAG (Retrieval-Augmented Generation):** Ideal para o cenário deste laboratório — busca dinâmica em bases de conhecimento que podem crescer ou mudar frequentemente.
* **⚡ CAG (Cache-Augmented Generation):** Quando os dados são estáticos e você quer latência zero, pré-carregando todo o texto na janela longa/KV Cache do modelo.
* **🧠 MAG (Memory-Augmented Generation):** Quando o agente precisa registrar e evoluir memórias sobre o usuário (ex: suas preferências de programação) entre diferentes execuções.

---

## 🛠️ Passo a Passo Prático

### 1. Instalação
Garanta que a dependência do banco vetorial local está instalada no seu ambiente:
```bash
pip install chromadb
```

### 2. Criar Cliente e Coleção Vetorial
Instanciamos o cliente e criamos a nossa "tabela" vetorial.
```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("secomp_workshop")
```

### 3. Inserir Documentos
Inserimos textos conceituais no banco. O ChromaDB calcula os embeddings semânticos automaticamente utilizando o modelo padrão `all-MiniLM-L6-v2`.
```python
collection.add(
    documents=[
        "RAG (Retrieval-Augmented Generation) busca informações dinamicamente em bancos vetoriais como o ChromaDB.",
        "CAG (Cache-Augmented Generation) pré-carrega conhecimento estático no KV Cache para resposta instantânea.",
        "MAG (Memory-Augmented Generation) retém memórias episódicas e preferências do usuário ao longo do tempo."
    ],
    ids=["doc_rag", "doc_cag", "doc_mag"]
)
```

### 4. Consulta Semântica
Fazemos a busca baseada no significado da pergunta em vez de palavras-chave exatas:
```python
results = collection.query(
    query_texts=["Qual técnica é melhor para dados estáveis e velocidade máxima?"],
    n_results=1
)

print("Documento mais relevante encontrado:")
print(results["documents"][0][0])
# Saída esperada: "CAG (Cache-Augmented Generation) pré-carrega conhecimento estático no KV Cache para resposta instantânea."
```
