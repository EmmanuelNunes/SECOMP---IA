# Entregável 6: Cheat Sheet RAG (Retrieval-Augmented Generation)

O **RAG** é uma técnica que fornece conhecimento externo e específico para Modelos de Linguagem, permitindo que eles consultem uma base de dados antes de responder a uma pergunta.

---

## ⚡ RAG no Ecossistema Moderno: RAG vs. CAG vs. MAG

Na engenharia de IA de 2026, o RAG é um dos três pilares fundamentais para gerenciamento de contexto:
* **🔍 RAG (Retrieval-Augmented Generation):** Ideal para **dados dinâmicos** que mudam frequentemente. Recupera pedaços de informação externa sob demanda.
* **⚡ CAG (Cache-Augmented Generation):** Ideal para **dados estáveis** onde a **velocidade/latência é crítica**. Mantém toda a base estática pré-carregada no KV Cache / contexto longo do modelo com resposta instantânea e custo reduzido.
* **🧠 MAG (Memory-Augmented Generation):** Ideal para **agentes com estado persistente**, retendo memórias episódicas, semânticas e preferências do usuário ao longo do tempo.

> 📖 *Para um comparativo detalhado, consulte o arquivo [`cheatsheets/RAG_vs_CAG_vs_MAG.md`](RAG_vs_CAG_vs_MAG.md).*

---

## O Pipeline Clássico de RAG

### 1. Documento (Ingestão)
A fonte crua de informação (ex: manuais em PDF, páginas web, datasets em JSONL). O primeiro passo é extrair o texto dessas fontes.

### 2. Chunking (Fragmentação)
Modelos de linguagem possuem limites práticos e benefícios de foco. O *chunking* quebra os documentos longos em "pedaços" (chunks) menores (ex: 500 palavras cada), mantendo a precisão das buscas e o overlap para preservar fronteiras contextuais.

### 3. Embedding (Vetorização)
Cada pedaço de texto é passado por um modelo de *Embedding* (como o `sentence-transformers`), que transforma o texto em um longo array de números (vetores). Esses números representam o **significado semântico** do texto. Textos com significados parecidos terão vetores próximos no espaço vetorial.

### 4. Vector DB (Banco Vetorial)
Os vetores gerados são armazenados em um Banco de Dados Vetorial (como **ChromaDB**, **FAISS**, **Qdrant** ou **Pinecone**). Ele é especializado em fazer cálculos matemáticos super rápidos (similaridade de cosseno) para encontrar vetores parecidos.

### 5. Retriever & Reranker (Recuperador e Reordenador)
Quando o usuário faz uma pergunta, o Retriever:
1. Converte a pergunta em um vetor (Embedding).
2. Pede ao Vector DB para buscar os "X" chunks mais similares à pergunta (Top-K).
3. (Opcional no RAG Avançado) Aplica um **Reranker** (Cross-Encoder) para refinar a precisão.
4. Recupera o texto desses chunks e envia para o LLM responder embasado neles!
