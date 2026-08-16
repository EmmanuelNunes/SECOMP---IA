# 📑 Cheat Sheet Definitivo: RAG vs. CAG vs. MAG (Arquiteturas de Contexto & Memória em IA)

> **Referência Técnica — SECOMP 2026**: Baseado na taxonomia de arquiteturas de IA de ponta para alocação de cargas de trabalho corporativas e sistemas multi-agentes.

---

## 🚦 09. Gatilhos de Decisão para Deploy em Produção

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🎯 MÉTRICAS DE DECISÃO RÁPIDA:                                                                              │
│                                                                                                             │
│ 1. Se os dados atualizam minuto a minuto e exigem rastreabilidade exata de fontes/citações:                │
│    👉 DEPLOY RAG (Retrieval-Augmented Generation)                                                           │
│                                                                                                             │
│ 2. Se os dados são amplamente estáticos e o tempo de resposta (sub-segundo) é a métrica primária:           │
│    👉 DEPLOY CAG (Cache-Augmented Generation)                                                               │
│                                                                                                             │
│ 3. Se a aplicação depende de agentes de raciocínio multi-etapas que rastreiam o estado do usuário ao tempo:│
│    👉 DEPLOY MAG (Memory-Augmented Generation)                                                              │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### ✅ Checklist de Condições de Ativação (Triggers)

| Critério | 🔍 RAG | ⚡ CAG | 🧠 MAG |
| :--- | :--- | :--- | :--- |
| **Volatilidade dos Dados** | Muda minuto a minuto | Estático / Raramente muda | Evolui continuamente com o uso |
| **Velocidade / Latência** | Latência moderada aceitável | **Ultra-rápida (Sub-segundo / TTFT $\approx$ 0ms)** | Variável conforme profundidade do grafo |
| **Tamanho da Base** | Bases distribuídas massivas (GBs/TBs) | Cabe na Janela de Contexto (VRAM) | Otimizado via Working Memory Window |
| **Rastreabilidade** | Citações e chunks exatos obrigatórios | Raciocínio holístico global | Histórico e decisões consolidadas |
| **Perfil da Tarefa** | Busca de dados frescos / externos | Q&A em livros, APIs, código congelado | Agentes multi-etapas, CRM, simulações |

---

## 🔬 01 a 03. Mecânica Interna e Fluxo de Execução

### 01. 🔍 RAG (Retrieval-Augmented Generation)
* **Conceito Chave:** Busca dinamicamente dados sem estado (*stateless*) fora de contexto a partir de índices externos em tempo de inferência.
* **Mecânica do Sistema (6 Etapas):**
  1. **User Query:** Usuário envia a pergunta ou instrução.
  2. **Embedding Model:** A query é convertida em um vetor denso que captura seu significado semântico.
  3. **Vector Database Search:** O embedding busca no banco vetorial (ChromaDB / Pinecone) os registros mais similares.
  4. **Context Payload (Top-K):** Os $K$ chunks mais relevantes são recuperados do banco.
  5. **LLM Engine:** O LLM recebe os chunks recuperados concatenados ao prompt para gerar a resposta.
  6. **Generated Response:** O modelo emite uma resposta contextualizada e embasada.

```text
[Usuário] ──> [Embedding Model] ──> [Busca Vetorial] <──> [(Vector DB)]
    │                                     │
    │                                     ▼ (Top-K Chunks)
    └─────────────────────────────> [LLM Engine] ──> [Resposta Embasada]
```

---

### 02. ⚡ CAG (Cache-Augmented Generation)
* **Conceito Chave:** Elimina totalmente a busca externa em tempo real ao pré-carregar e fixar a base de documentos inteira diretamente no **KV-Cache** da memória GPU do LLM.
* **Mecânica do Sistema (6 Etapas):**
  1. **Document Store:** Toda a documentação e fontes de conhecimento são coletadas.
  2. **Pre-Loaded Context:** Todo o acervo documental é processado e carregado na janela de contexto de antemão.
  3. **GPU VRAM KV-Cache (Frozen):** O contexto pré-carregado é armazenado na VRAM da GPU como KV-Cache congelado (*frozen*).
  4. **User Query:** O usuário submete a pergunta.
  5. **LLM Attention Layer Execution:** A camada de atenção do LLM atende instantaneamente sobre o contexto em cache e a query.
  6. **Rapid Response:** Como não há busca externa nem I/O de rede, a resposta é gerada em velocidade nativa de hardware.

```text
[Base Documental] ──> [Pré-carga Contextual] ──> [GPU VRAM KV-Cache (Frozen)]
                                                           │
[Pergunta Usuário] ────────────────────────────────────────┼──> [Camada de Atenção LLM] ──> [⚡ Resposta Instantânea]
```

---

### 03. 🧠 MAG (Memory-Augmented Generation)
* **Conceito Chave:** Implementa tabelas de memória persistentes e graváveis (*read/write*) em paralelo à pipeline de inferência para rastrear estados mutáveis de sessão em loops de agentes multi-etapas (*multi-hop*).
* **Mecânica do Sistema (6 Etapas):**
  1. **User Query:** Usuário fornece a instrução ou meta.
  2. **Read Memory:** O estado e contexto passado relevante são lidos das tabelas de memória (*State Fetch*).
  3. **LLM Inference:** O LLM gera uma ação ou resposta intermediária baseando-se na query e na memória recuperada.
  4. **Write Memory:** Novas informações, decisões e aprendizados são gravados de volta nas tabelas de memória.
  5. **Agent Loop:** O agente continua seu loop de execução multi-hop utilizando a memória atualizada.
  6. **Final Response:** O resultado final consolidado é retornado ao usuário.

```text
[Usuário] ──> [Leitura de Memória] <─── [(Tabelas de Memória Persistentes R/W)]
                     │                                   ▲
                     ▼                                   │
             [Inferência LLM] ──> [Escrita de Memória] ──┘
                     │
                     ▼
             [Loop do Agente] ──> [Resposta Final]
```

---

## 🏛️ 04. Comparação Estrutural de Paradigmas

| Vetor Arquitetural | 🔍 RAG | ⚡ CAG | 🧠 MAG |
| :--- | :--- | :--- | :--- |
| **Origem do Conhecimento** | Espaço de Índice Externo (*External Index*) | Janela de Contexto Sem Limites (*Boundless Window*) | Matrizes de Memória Inline (*Memory Matrices*) |
| **Estado Operacional** | **Completamente Sem Estado** ($\times$ *Stateless*) | **Pré-Compilado / Congelado** (❄️ *Pre-baked / Frozen*) | **Altamente Com Estado & Mutável** ($\circlearrowleft$ *Stateful & Mutating*) |
| **Principal Dreno de Latência** | I/O de Rede com Banco de Dados (*Network I/O*) | Processamento Inicial do Prompt (*Prompt Ingestion*) | Roteamento do Controlador de Memória (*Memory Routing*) |
| **Sincronização de Dados** | **Instantânea** (Atualização de Índice ⚡) | **Em Lote** (Invalidação de Cache 📅) | **Contínua** (Operações de Escrita R/W ✏️) |

---

## ⏱️ 05. Perfil Detalhado de Latência (Time-to-First-Token - TTFT)

```text
⚡ CAG: [User Prompt] ──> [Pre-loaded KV-Cache (No Lookup)] ─────────> [TTFT ≈ 0ms] ──> [LLM Execution @ Native GPU Speed] ──> Tokens
   Velocidade: ⚡ ULTRA-RÁPIDA (Elimina busca externa, I/O e vetorização).

🔍 RAG: [User Prompt] ──> [Query Embedding] ──> [Vector DB Lookup] ──> [Top-K Ranking] ──> [Network] ──> [TTFT] ──> [LLM Gen] ──> Tokens
   Velocidade: 🟡 MODERADA (Gargalo no pipeline de recuperação e rede antes do 1º token).

🧠 MAG: [User Prompt] ──> [Read Memory] ──> [Validation & Consistency] ──> [LLM + State] ──> [Write Memory] ──> [TTFT] ──> [LLM] ──> Tokens
   Velocidade: 🟣 VARIÁVEL (Depende da profundidade do grafo de agentes e validação de consistência R/W).
```

---

## 📐 06. Limites de Escala e Topologia de Contexto

```text
┌───────────────────────────────────┬───────────────────────────────────┬───────────────────────────────────┐
│ 🔍 RAG: Topologia Externa         │ ⚡ CAG: Topologia em VRAM         │ 🧠 MAG: Topologia Swapping        │
├───────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────┤
│ [Doc Pool Gigante: GBs/TBs]       │ [Janela do LLM: 1M a 2M tokens]   │ [Tabelas de Memória Persistentes] │
│          │                        │         │                         │          │ (Load)     ▲ (Evict)   │
│          ▼ (Top-K Filter)         │         ▼ (Leitura Direta)        │          ▼            │           │
│ [Contexto Pequeno para o LLM]     │ [Execução na VRAM da GPU]         │ [Working Memory Window Dinâmica]  │
│                                   │                                   │          │                        │
│ • Escala virtualmente infinita    │ • Limitado pelo tamanho da janela │ • Escala via gerência dinâmica    │
│ • Custo controlado por Top-K      │ • Depende de GPUs com alta VRAM   │ • Mantém performance em multi-turn│
│ • Depende da precisão do índice   │ • Desempenho 100% previsível      │ • Evita degradação de contexto    │
└───────────────────────────────────┴───────────────────────────────────┴───────────────────────────────────┘
```

---

## 💼 07. Alocação de Cargas de Trabalho em Produção

```text
┌───────────────────────────────────┬───────────────────────────────────┬───────────────────────────────────┐
│ 🔍 RAG: Dados Vivos & Dinâmicos   │ ⚡ CAG: Dados Estáticos & Código  │ 🧠 MAG: Engenharia Multi-Agente   │
├───────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────┤
│ • Documentos Corporativos Vivos   │ • Manuais e Livros Didáticos      │ • Sistemas Multi-Agentes          │
│   (Políticas, POPs, processos)    │   (Materiais de referência fixos) │   (Agentes com metas e contexto)  │
│ • Jurídico e Conformidade         │ • Repositórios de Código Longos   │ • Automação de Contas de Clientes │
│   (Leis, jurisprudências, normas) │   (Codebases inteiras em cache)   │   (Histórico, CRM, preferências)  │
│ • Bases de Pesquisa & Arquivos    │ • Aplicações de Baixa Latência    │ • Fluxos Avançados de Dev         │
│   (Milhões de arquivos e wikis)   │   (Sistemas com resposta < 1 seg) │   (Agentes de refatoração, CI/CD) │
│ • Dados Externos em Tempo Real    │ • Dados Estáveis / Congelados     │ • Simulações e Longas Sessões     │
│   (Mercado financeiro, notícias)  │   (Imutáveis, perfeitos p/ cache) │   (Manutenção de estado e mundo)  │
└───────────────────────────────────┴───────────────────────────────────┴───────────────────────────────────┘
```

---

## 💰 08. Infraestrutura e Pegada de Recursos (Matriz 2x2)

```text
                      ALTO CUSTO DE DEPLOYMENT (Compute + Operações)
                                            ▲
                                            │
                     ┌──────────────────────┼──────────────────────┐
                     │ 🔍 RAG               │ 🧠 MAG               │
                     │ Custo Moderado       │ Alto Custo           │
                     │ Baixa Complexidade   │ Alta Complexidade    │
                     └──────────────────────┼──────────────────────┘
  BAIXA COMPLEXIDADE ───────────────────────┼───────────────────────> ALTA COMPLEXIDADE
  (Fácil de Construir)                      │                        (Difícil de Manter)
                     ┌──────────────────────┼──────────────────────┐
                     │ ⚡ CAG               │                      │
                     │ Alto Custo Inicial   │                      │
                     │ Baixa Complexidade   │                      │
                     └──────────────────────┼──────────────────────┘
                                            │
                                            ▼
                     BAIXO CUSTO DE DEPLOYMENT (Compute + Operações)
```

### Detalhamento de Custos e Perfis de Hardware

* **🔍 RAG:**
  * **Cost Drivers:** Armazenamento e escalabilidade do Vector DB, chamadas de embedding, tráfego de rede, rotinas de reindexação.
  * **Perfil de Hardware:** Roda eficientemente com LLMs menores e servidores convencionais (CPUs / GPUs de entrada).
* **⚡ CAG:**
  * **Cost Drivers:** Alto consumo de VRAM, instâncias de GPU ativas 24/7 (A100/H100), custos de reaquecimento de cache na invalidação.
  * **Perfil de Hardware:** Exige servidores GPU corporativos com memória massiva e modelos com suporte a janelas longas (Gemini 3.7 Flash, Claude 3.5).
* **🧠 MAG:**
  * **Cost Drivers:** Desenvolvimento de controladores de memória customizados, camada de persistência de estado, algoritmos de sumarização e resolução de conflito.
  * **Perfil de Hardware:** Necessidade moderada a alta de VRAM combinada com bancos de chave-valor/grafos de baixa latência (Redis, Mem0, PostgreSQL).
