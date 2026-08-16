# 🚀 Apostila Oficial: Workshop de IA e Agentes Autônomos (SECOMP 2026)

Bem-vindo(a) à apostila oficial do **Workshop de IA e Agentes Autônomos** da **SECOMP 2026**! Este material foi elaborado e atualizado com base nos conceitos mais recentes de Inteligência Artificial Generativa, Agentes Autônomos, o protocolo **MCP (Model Context Protocol)** e arquiteturas de recuperação **RAG Avançado (Hybrid & GraphRAG)**.

> [!NOTE]
> **Créditos, Orientação e Agradecimentos Especiais:**
> Este material e a metodologia adotada possuem fundamentação acadêmica e conceitual nos trabalhos, pesquisas e ferramentas desenvolvidas pelo **Prof. M.Sc. Sanderson Oliveira de Macedo (Prof. Sandeco)** — Instituto Federal de Goiás (IFG) / Universidade Federal de Goiás (UFG), criador do [Canal Sandeco](https://youtube.com/canalsandeco), do framework [Reversa](https://github.com/sandeco/reversa) e do ecossistema [Mira](https://github.com/sandeco/mira-animator), e pelo **Prof. Dr. Carlos Alex Sander Juvêncio Gulo** — Universidade do Estado de Mato Grosso (UNEMAT) / Universidade do Porto (FEUP), líder do [Grupo de Pesquisa PIXEL](http://dgp.cnpq.br/dgp/espelhogrupo/510344).

---

## 📌 Sumário
1. [Módulo 1: Introdução aos LLMs & Modelos de Raciocínio (2026)](#1-módulo-1-introdução-aos-llms--modelos-de-raciocínio-2026)
1.1 [Módulo 1.1: Guia de Prompting no Google Workspace com Gemini](#11-módulo-11-guia-de-prompting-no-google-workspace-com-gemini)
1.2 [Módulo 1.2: O Modelo Vigente: Gemini 3.7 Flash & Raciocínio Híbrido](#12-módulo-12-o-modelo-vigente-gemini-37-flash--raciocínio-híbrido)
2. [Módulo 2: Engenharia de Prompts de Elite & Outputs Estruturados](#2-módulo-2-engenharia-de-prompts-de-elite--outputs-estruturados)
3. [Módulo 3: Model Context Protocol (MCP - Especificação Aberta)](#3-módulo-3-model-context-protocol-mcp---especificação-aberta)
4. [Módulo 4: Agentes Autônomos, Agent Harnesses, Framework Reversa & Antigravity](#4-módulo-4-agentes-autônomos-agent-harnesses-framework-reversa--antigravity)
5. [Módulo 5: RAG Avançado, Paradigmas de Contexto (RAG vs. CAG vs. MAG) & GraphRAG](#5-módulo-5-rag-avançado-paradigmas-de-contexto-rag-vs-cag-vs-mag--graphrag)
6. [Módulo 6: Segurança, Governança & OWASP Top 10 para LLMs](#6-módulo-6-segurança-governança--owasp-top-10-para-llms)
7. [Módulo 7: Projeto Prático Integrador — Career-AI (MVP 2026)](#7-módulo-7-projeto-prático-integrador---career-ai-mvp-2026)
8. [Módulo 8: Referências Acadêmicas & Trabalhos dos Professores Sanderson Macedo e Carlos Alex Sander Gulo](#8-módulo-8-referências-acadêmicas--trabalhos-dos-professores-sanderson-macedo-e-carlos-alex-sander-gulo)

---

## 1. Módulo 1: Introdução aos LLMs & Modelos de Raciocínio (2026)

Os **Grandes Modelos de Linguagem (LLMs)** evoluíram para sistemas altamente sofisticados capazes de raciocínio lógico em tempo de inferência (*Test-Time Compute*), arquiteturas de mistura de especialistas (*Mixture of Experts - MoE*) e execução nativa multimodal.

### A Evolução Arquitetural
* **Transformers Clássicos (2017-2023):** Processamento baseado unicamente em self-attention de passo único.
* **Mixture of Experts - MoE (2024-2025):** Ativação seletiva de sub-redes (especialistas) reduzindo custo computacional enquanto amplia parâmetros totais.
* **Modelos de Raciocínio (Reasoning Models / 2025-2026):** Modelos que utilizam cadeias de pensamento internas (*Chain-of-Thought*) expandidas antes de emitir a resposta final, resolvendo problemas complexos de código, matemática e lógica formal.

### Principais Capacidades Modernas
1. **Janelas de Contexto Gigantescas:** Suporte a 1M até 10M+ tokens de contexto (ex: ecossistema Gemini), permitindo carregar repositórios inteiros de código em uma única chamada.
2. **Multimodalidade Nativa:** Processamento e geração síncrona de texto, imagens, áudio e vídeo (real-time voice & vision).
3. **Structured Outputs (Saídas Garantidas):** Garantia matemática de conformidade com schemas JSON/Pydantic na camada de amostragem de tokens.

---

## 1.1. Módulo 1.1: Guia de Prompting no Google Workspace com Gemini

A integração da IA Generativa no Google Workspace une modelos de última geração aos dados institucionais em um ambiente seguro e em conformidade com a privacidade.

### Ecossistema Gemini no Workspace
1. **Aplicativos AI-First:**
   * **Gemini App (Corporate):** Chat com suporte a *Deep Research* (agente autônomo de pesquisa profunda) e *Canvas* (ambiente de edição iterativa).
   * **NotebookLM:** Assistente de pesquisa baseado nos seus documentos do Google Drive, PDFs e notas, oferecendo resumos e o *Audio Overview* (podcasts gerados via IA baseados nos seus textos).
   * **Google Vids:** Ferramenta de criação de apresentações e vídeos interativos baseados em IA.
2. **Painel Lateral Embutido:** Acesso in-line no Gmail, Docs, Slides, Sheets e Drive com grounding dinâmico via marcação `@`.

> [!IMPORTANT]
> **Governança e Privacidade:** Os dados corporativos processados pelo Gemini no Workspace **não são utilizados para treinamento de modelos públicos**, não passam por revisão humana e permanecem protegidos por criptografia de nível enterprise.

---

## 1.2. Módulo 1.2: O Modelo Vigente: Gemini 3.7 Flash & Raciocínio Híbrido

O **Gemini 3.7 Flash** representa o estado da arte dos modelos de linguagem da Google em 2026, sendo o primeiro modelo de **Raciocínio Híbrido (*Hybrid Reasoning Engine*)** de classe mundial.

```mermaid
graph LR
    Input[Entrada / Prompt do Usuário] --> Router{Complexidade da Tarefa}
    Router -->|Baixa Complexidade / Velocidade| FlashMode[🚀 Standard Flash Mode: Resposta Instantânea & Baixo Custo]
    Router -->|Alta Complexidade / Codificação| ThinkingMode[🧠 Thinking Mode: Test-Time Compute & Cadeia de Raciocínio Profunda]
    FlashMode --> Output[Resposta Otimizada]
    ThinkingMode --> Output
```

### Principais Inovações do Gemini 3.7 Flash
1. **Unificação de Velocidade e Profundidade:** Elimina a necessidade de escolher entre um modelo ultra-rápido (como os modelos Flash anteriores) e um modelo lento de raciocínio puro. Ele opera nativamente em ambos os regimes através do controle de *Thinking Budget* (orçamento de pensamento ajustável).
2. **Liderança em Engenharia de Software e Agentes:** Desempenho de ponta na resolução autônoma de issues complexas em repositórios reais (benchmarks SWE-bench), refatorações arquiteturais e geração de código livre de bugs.
3. **Context Caching Nativo de Alta Eficiência:** Permite que 1 Milhão de tokens de documentação e código sejam mantidos em memória de inferência com custo até 90% menor e Time-To-First-Token (TTFT) instantâneo.
4. **Chamada de Ferramentas de Primeira Classe:** Integração nativa com o protocolo MCP e ferramentas de sistema com rigorosa validação de tipos e structured outputs.


## 2. Módulo 2: Engenharia de Prompts de Elite & Outputs Estruturados

A **Engenharia de Prompts** é o projeto rigoroso de interfaces de entrada/saída para componentes de software de IA.

### Os 5 Pilares de um Prompt Profissional (Prompting 101)

| Pilar | Descrição | Exemplo Prático |
| :--- | :--- | :--- |
| **Persona (Papel)** | Identidade técnica ou executiva assumida pelo LLM. | *"Você é um Diretor de Tecnologia especializado em microsserviços."* |
| **Task (Tarefa)** | Ação principal detalhada iniciada por verbo no imperativo. | *"Escreva um documento de arquitetura referente à migração do sistema."* |
| **Context (Contexto)** | Informações de fundo, restrições e cenário de negócio. | *"Considerando que a equipe possui 5 desenvolvedores e utiliza AWS."* |
| **Constraints (Restrições)** | Limites que o modelo NÃO pode ultrapassar. | *"Não utilize bibliotecas obsoletas. Não invente credenciais."* |
| **Format (Formato)** | Estrutura visual exata da saída esperada. | *"Responda em formato Markdown com diagramas Mermaid e tabelas."* |

---

## 3. Módulo 3: Model Context Protocol (MCP - Especificação Aberta)

O **Model Context Protocol (MCP)** é o padrão aberto mantido sob governança da Linux Foundation (criado originalmente pela Anthropic) que revoluciona como os LLMs se conectam ao mundo externo.

### Arquitetura de Comunicação do MCP
```mermaid
graph LR
    Agent[Agente / IDE Cliente] <--> |MCP Protocol (Stdio / SSE)| MCPServer[MCP Server]
    MCPServer <--> Tools[Tools: APIs / GitHub / Terminal]
    MCPServer <--> Resources[Resources: DBs / Filesystem]
    MCPServer <--> Prompts[Prompts: Templates do Servidor]
```

### As 3 Abstrações Principais
1. **Tools (Ferramentas):** Funções executáveis com parâmetros validados por JSON Schema que o LLM pode invocar autonomamente.
2. **Resources (Recursos):** Fontes de dados expostas via URIs (`file://`, `postgres://`, `github://`) para leitura passiva pelo modelo.
3. **Prompts:** Modelos e fluxos reutilizáveis definidos pelo servidor.

---

## 4. Módulo 4: Agentes Autônomos, Agent Harnesses, Framework Reversa & Antigravity

Um **Agente de IA** é um sistema computacional que utiliza um LLM como motor de raciocínio central para perceber um objetivo, planejar ações, executar ferramentas em loop e ajustar sua conduta.

### 4.1. O Conceito de Agent Harness (Macedo, 2026)
Conforme definido pelo Prof. Sanderson Macedo no artigo *"What makes a harness a harness"* (arXiv:2606.10106), o **Agent Harness** é a camada de software que envolve um modelo de linguagem e o capacita a atuar diretamente sobre repositórios de código com isolamento, ciclo de vida e controle de execução.

### 4.2. O Framework Reversa (Macedo & Costa, 2026)
Desenvolvido pelo Prof. Sanderson Macedo, o **Reversa** ([github.com/sandeco/reversa](https://github.com/sandeco/reversa), arXiv:2605.18684) é um framework de engenharia reversa de documentação que converte sistemas legados em especificações operacionais rastreáveis e executáveis por agentes de IA através de uma pipeline multi-agente:

```mermaid
graph TD
    Legacy[Código Legado / Sistema Antigo] --> Surface[Agente de Mapeamento de Superfície]
    Surface --> Rules[Agente de Extração de Regras Implícitas]
    Rules --> Spec[Agente Gerador de Especificações]
    Spec --> Gherkin[Cenários de Paridade Gherkin + Testes para Agentes]
```

### 4.3. Ambientes de Desenvolvimento Agêntico: Google Antigravity (AGY)
O **Google Antigravity (AGY)** é a plataforma avançada concebida pela equipe do Google DeepMind que operacionaliza o desenvolvimento agêntico na prática, integrando ferramentas de terminal, subagentes especializados e modelos de raciocínio como o **Gemini 3.7 Flash**.

```mermaid
flowchart LR
    Dev([Desenvolvedor]) <--> Antigravity[🤖 Google Antigravity Core]
    Antigravity <--> Subagents[👥 Subagentes Concorrentes & Workspaces]
    Antigravity <--> Skills[🧩 Skills Modulares: SKILL.md]
    Antigravity <--> Rules[📜 Governança: AGENTS.md / GEMINI.md]
    Antigravity <--> MCP[🔌 Integração Nativa MCP]
```

#### Pilares do Antigravity na SECOMP 2026:
1. **Subagentes Hierárquicos e Concorrentes:** Capacidade de lançar subagentes em segundo plano (`research`, `self`, ou customizados em tempo de execução via `define_subagent`) com isolamento de repositório (*workspaces* `branch` / `share` / `inherit`).
2. **Sistema de Skills Encapsuladas:** Habilidades modulares compostas por `SKILL.md` (metadados YAML), scripts em Python/Shell e materiais de referência carregados dinamicamente sob demanda.
3. **Governança por Regras Vivas (`AGENTS.md`):** Arquivos declarativos na raiz do projeto que ditam a conduta, restrições e padrões arquiteturais que nenhum subagente pode violar.
4. **Rastreabilidade e Artefatos:** Geração de documentos vivos (`artifacts`), diffs contínuos e auditoria passo a passo via arquivos de transcrição (`transcript.jsonl`).


---

## 5. Módulo 5: RAG Avançado, Paradigmas de Contexto (RAG vs. CAG vs. MAG) & GraphRAG

O **RAG (Retrieval-Augmented Generation)** é a técnica essencial para fundamentar LLMs em dados corporativos atualizados, eliminando alucinações. Contudo, no estado da arte de 2026, a gestão de contexto evoluiu para três paradigmas complementares: **RAG**, **CAG** e **MAG**.

### 5.1. O Pipeline Clássico e Avançado de RAG

```mermaid
flowchart TD
    Doc[Documentos Corporativos] --> SemanticChunking[Semantic Chunking]
    SemanticChunking --> DenseEmbed[Dense Vectors - Sentence Transformers]
    SemanticChunking --> SparseIndex[Sparse Index - BM25 Keywords]
    DenseEmbed --> VectorDB[Vector DB - ChromaDB]
    
    Query[Pergunta do Usuário] --> HybridSearch[Hybrid Search & RRF Fusion]
    VectorDB --> HybridSearch
    SparseIndex --> HybridSearch
    
    HybridSearch --> Reranker[Cohere / BGE Reranker]
    Reranker --> TopKContext[Top-K Contextos Limpos]
    TopKContext --> LLM[LLM Generator]
    LLM --> FinalAnswer[Resposta Embasada e Fiel]
```

#### Tecnologias do RAG Avançado
1. **Hybrid Search (Busca Híbrida):** Combinação de busca vetorial densa com busca esparsa BM25 unificadas por *Reciprocal Rank Fusion (RRF)*.
2. **Reranking:** Reordenação precisa dos fragmentos de texto via modelos *Cross-Encoder*.
3. **GraphRAG:** Integração de Grafos de Conhecimento com busca vetorial para sintetizar dados complexos interconectados.

---

### 5.2. O Grande Dilema Arquitetural: RAG vs. CAG vs. MAG

A decisão arquitetural mais importante em sistemas de IA e agentes em 2026 não é eleger o "melhor" método, mas sim **escolher a arquitetura correta para a dinâmica da carga de trabalho**:

```mermaid
graph LR
    Need[Requisito do Sistema] -->|Dados mudam minuto a minuto?| RAG[🔍 RAG: Retrieval-Augmented]
    Need -->|Dados estáveis + Baixa Latência?| CAG[⚡ CAG: Cache-Augmented]
    Need -->|Agente precisa de estado persistente?| MAG[🧠 MAG: Memory-Augmented]
```

#### 1. 🔍 RAG (Retrieval-Augmented Generation) — Dados Dinâmicos & Grandes Escalas
* **Mecânica:** Busca dinamicamente dados *stateless* e fora de contexto a partir de índices externos em tempo de query via similaridade vetorial (ChromaDB, Pinecone).
* **Vetor Arquitetural:** Origem do conhecimento em espaço de índice externo; estado operacional 100% *stateless*; dreno de latência no I/O de rede com banco de dados; sincronização de dados instantânea por atualização de índice.
* **Quando Usar:** Bases documentais vivas, conformidade jurídica com atualizações constantes, pesquisa sobre milhões de arquivos e dados de mercado em tempo real.

#### 2. ⚡ CAG (Cache-Augmented Generation) — Dados Estáticos & Latência Zero
* **Mecânica:** Bypassa completamente a busca externa ao pré-carregar e fixar todo o acervo documental diretamente no **KV-Cache congelado (*frozen*)** na VRAM da GPU do LLM.
* **Vetor Arquitetural:** Origem do conhecimento na janela de contexto longa (1M--2M tokens); estado pré-compilado/congelado; dreno de latência limitado à ingestão inicial; sincronização de dados em lote por invalidação de cache.
* **Quando Usar:** Manuais e livros didáticos, bases de código congeladas para copilotos de repositório inteiro, ferramentas internas com dados fixos e aplicações com requisito de resposta sub-segundo (TTFT $\approx$ 0ms).

#### 3. 🧠 MAG (Memory-Augmented Generation) — Memória Evolutiva & Continuidade de Agentes
* **Mecânica:** Implementa tabelas de memória persistentes e graváveis (*read/write*) em paralelo à pipeline de inferência para rastrear estados mutáveis de sessão em loops de agentes multi-etapas.
* **Vetor Arquitetural:** Origem em matrizes de memória inline; estado altamente mutável e com estado (*stateful*); dreno de latência no roteamento do controlador de memória; sincronização contínua por operações de escrita.
* **Quando Usar:** Engenharia de software multi-agente, automação de contas/CRM de clientes, fluxos de desenvolvimento com agentes autônomos e simulações de longa duração.

---

### 5.3. Comparativo Estrutural e Perfil de Latência (TTFT)

| Vetor Arquitetural | 🔍 RAG | ⚡ CAG | 🧠 MAG |
| :--- | :--- | :--- | :--- |
| **Origem do Conhecimento** | Espaço de Índice Externo | Janela de Contexto Sem Limites | Matrizes de Memória Inline |
| **Estado Operacional** | Totalmente Sem Estado (*Stateless*) | Pré-compilado / Congelado (*Frozen*) | Altamente Com Estado (*Stateful*) |
| **Principal Dreno de Latência** | I/O de Rede com Banco de Dados | Processamento Inicial de Ingestão | Roteamento do Controlador de Memória |
| **Sincronização de Dados** | Instantânea (Atualização de Índice) | Em Lote (Invalidação de Cache) | Contínua (Operações de Escrita R/W) |
| **Perfil de Velocidade** | Moderada (Pipeline multi-etapas) | **⚡ Mais Rápida (TTFT $\approx$ 0ms)** | Variável (Depende do grafo de agentes) |

---

### 5.4. Topologia de Memória, Escala e Matriz de Infraestrutura (2x2)

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

* **🔍 RAG:** Escala virtualmente infinita via índices externos; custo controlado por filtragem Top-K; roda com LLMs menores e hardware padrão.
* **⚡ CAG:** Escala limitada pelo tamanho da janela de contexto e VRAM de GPU (A100/H100); custo inicial mais alto para manter instâncias ativas, compensado pelo custo 90% menor por token processado e latência zero.
* **🧠 MAG:** Otimiza a janela de contexto local gerenciando *Working Memory Windows* (carrega novos tokens e expulsa tokens antigos) para evitar degradação de estado ao longo de ciclos profundos.

---

### 5.5. Gatilhos de Deploy em Produção (Decision Triggers)

1. **Ative RAG quando:** Dados atualizam minuto a minuto; exigência de citações precisas de fontes; bases massivas e distribuídas com múltiplos contribuidores.
2. **Ative CAG quando:** Dados são amplamente estáveis ou raramente mudam; resposta ultrarrápida (sub-segundo) é a prioridade número um; dados cabem na janela do modelo.
3. **Ative MAG quando:** A aplicação exige raciocínio multi-etapas com ferramentas; necessidade de rastrear e atualizar o perfil do usuário/sessão ao longo do tempo.



---

## 6. Módulo 6: Segurança, Governança & OWASP Top 10 para LLMs

A segurança em sistemas com LLMs requer proteções contra ameaças atípicas ao software tradicional.

### O Top 4 de Vulnerabilidades em Sistemas com LLM (OWASP)
1. **Prompt Injection (Direta e Indireta):** Delimitação XML estrita e sanitização de inputs.
2. **Data Leakage (Vazamento de PII):** Controle de acesso RBAC no Vector DB e mascaramento prévio.
3. **Excessive Agency (Agência Excessiva):** Princípio do Menor Privilégio e aprovação humana (Human-in-the-Loop - HITL).
4. **Guardrails Ativos:** Filtros de entrada e saída operando em milissegundos (NeMo Guardrails / Llama Guard).

---

## 7. Módulo 7: Projeto Prático Integrador — Career-AI (MVP 2026)

O **Career-AI** é a aplicação prática desenvolvida no workshop que consolida todos os conceitos em uma solução end-to-end completa (FastAPI + ChromaDB + Agentes LangGraph + Frontend Web).

---

## 8. Módulo 8: Referências Acadêmicas & Trabalhos dos Professores Sanderson Macedo e Carlos Alex Sander Gulo

Este workshop e seu material didático referenciam, incorporam e agradecem as seguintes contribuições acadêmicas, bibliográficas e de pesquisa:

### 8.1. Contribuições do Prof. M.Sc. Sanderson Oliveira de Macedo (Prof. Sandeco)
*Instituto Federal de Goiás (IFG) / Universidade Federal de Goiás (UFG)*

1. **MACEDO, Sanderson Oliveira de.** *What makes a harness a harness: necessary and sufficient conditions for an agent harness.* arXiv preprint arXiv:2606.10106, 2026. Disponível em: [https://arxiv.org/abs/2606.10106](https://arxiv.org/abs/2606.10106).
2. **MACEDO, Sanderson Oliveira de.** *From Prompt to Process: a Process Taxonomy and Comparative Assessment of Frameworks Supporting AI Software Development Agents.* arXiv preprint arXiv:2606.04967, 2026. Disponível em: [https://arxiv.org/abs/2606.04967](https://arxiv.org/abs/2606.04967).
3. **MACEDO, Sanderson Oliveira de; COSTA, Ronaldo Martins da.** *Reversa: A Reverse Documentation Engineering Framework for Converting Legacy Software into Operational Specifications for AI Agents.* arXiv preprint arXiv:2605.18684, 2026. Disponível em: [https://arxiv.org/abs/2605.18684](https://arxiv.org/abs/2605.18684).
4. **MACEDO, Sanderson Oliveira de.** Repositórios de código e projetos open-source em IA e Agentes Autônomos. GitHub: [github.com/sandeco](https://github.com/sandeco).
5. **CANAL SANDECO.** Conteúdo audiovisual, aulas e tutoriais sobre Inteligência Artificial, Aprendizado por Reforço e Agentes. YouTube: [youtube.com/canalsandeco](https://youtube.com/canalsandeco).

### 8.2. Contribuições do Prof. Dr. Carlos Alex Sander Juvêncio Gulo
*Universidade do Estado de Mato Grosso (UNEMAT) / Universidade do Porto (FEUP) / Grupo PIXEL*

1. **GULO, Carlos Alex Sander Juvêncio.** *High-Performance Computing and Image Processing Architectures for Interactive and Medical Systems.* Tese (Doutoramento em Engenharia Informática) — Faculdade de Engenharia da Universidade do Porto (FEUP / INEGI), Porto, Portugal, 2019.
2. **GULO, Carlos Alex Sander Juvêncio; GRUPO PIXEL.** *Processamento de Imagens Médicas, Visão Computacional e Segmentação Semântica de Alta Resolução.* Diretório dos Grupos de Pesquisa no Brasil (CNPq / UNEMAT), 2020--2026. Disponível em: [http://dgp.cnpq.br/dgp/espelhogrupo/510344](http://dgp.cnpq.br/dgp/espelhogrupo/510344).
3. **GULO, Carlos Alex Sander Juvêncio et al.** *Robótica Educacional, Inteligência Artificial e Ambientes Interativos de Ensino Colaborativo em Computação.* Escola Regional de Informática de Mato Grosso (ERI-MT) / Sociedade Brasileira de Computação (SBC), 2018--2026.
4. **GULO, Carlos Alex Sander Juvêncio.** *Currículo do Sistema de Currículos Lattes (CNPq).* Disponível em: [http://lattes.cnpq.br/0062065110639984](http://lattes.cnpq.br/0062065110639984).
5. **GULO, Carlos Alex Sander Juvêncio.** Produção Científica e Perfil no ResearchGate. Disponível em: [https://www.researchgate.net/profile/Carlos-Gulo](https://www.researchgate.net/profile/Carlos-Gulo).

---
---

## 👨‍💻 Mantenedores e Equipe
* **Emmanuel Nunes** - Instrutor e Desenvolvedor ([GitHub](https://github.com/EmmanuelNunes))
* **Prof. Dr. Carlos Alex Sander Juvêncio Gulo** - Professor, Pesquisador e Orientador (UNEMAT / Grupo PIXEL)

---
*Apostila do Workshop SECOMP 2026 — Ministrada por Emmanuel Nunes com co-autoria, apoio e orientação do Prof. Dr. Carlos Alex Sander Juvêncio Gulo e referencial metodológico do Prof. Sanderson Macedo.* 💙