# Entregável 6: Cheat Sheet RAG (Retrieval-Augmented Generation)

O **RAG** é uma técnica que fornece memória extra e específica para Modelos de Linguagem, permitindo que eles consultem uma base de dados antes de responder a uma pergunta.

## O Pipeline Clássico de RAG

### 1. Documento
A fonte crua de informação (ex: manuais em PDF, páginas web, datasets em JSONL). O primeiro passo é extrair o texto dessas fontes.

### 2. Chunking (Fragmentação)
Modelos de linguagem não conseguem ler milhares de páginas de uma vez. O *chunking* quebra os documentos longos em "pedaços" (chunks) menores (ex: 500 palavras cada), mantendo a precisão das buscas.

### 3. Embedding (Vetorização)
Cada pedaço de texto é passado por um modelo de *Embedding* (como o `sentence-transformers`), que transforma o texto em um longo array de números (vetores). Esses números representam o **significado semântico** do texto. Textos com significados parecidos terão vetores próximos.

### 4. Vector DB (Banco Vetorial)
Os vetores gerados são armazenados em um Banco de Dados Vetorial (como **ChromaDB**, **FAISS** ou **Pinecone**). Ele é especializado em fazer cálculos matemáticos super rápidos para encontrar vetores parecidos.

### 5. Retriever (Recuperador)
Quando o usuário faz uma pergunta, o Retriever:
1. Converte a pergunta em um vetor (Embedding).
2. Pede ao Vector DB para buscar os "X" chunks mais similares à pergunta.
3. Recupera o texto desses chunks e envia para o LLM responder embasado neles!
