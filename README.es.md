[Português (Brasil)](README.md) · [English](README.en.md) · **Español**

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="docs/assets/readme/hero-still.svg">
  <img src="docs/assets/readme/hero.svg" alt="SECOMP 2026 Workshop Banner" width="1600" height="680">
</picture>

# Workshop de IA e Agentes Autônomos (SECOMP 2026)

**Repositório oficial de aulas, materiais conceituais e laboratórios práticos do Workshop de IA e Agentes Autônomos da SECOMP 2026.**

Do modelo conceitual de LLMs à orquestração prática de agentes de IA, RAG multimodal, apresentações coreografadas em Mira D3.js e sistemas cognitivos aplicados no projeto integrador **Career-AI**.

<p align="center"><a href="#start"><strong>COMEÇAR AGORA →</strong></a> &nbsp; · &nbsp; <a href="#labs"><strong>LABORATÓRIOS</strong></a> &nbsp; · &nbsp; <a href="#architecture"><strong>ARQUITETURA</strong></a> &nbsp; · &nbsp; <a href="#career-ai"><strong>CAREER-AI</strong></a> &nbsp; · &nbsp; <a href="#research"><strong>REFERÊNCIAS ACADÊMICAS</strong></a></p>

---

<a id="start"></a>
## 00 / Escolha onde começar

| Trilha do participante | Ponto de partida | Entregável / Foco |
|---|---|---|
| **Apostila e Teoria** | [`apostila/`](apostila) | Material conceitual completo de fundamentos, arquiteturas e agentes. |
| **Cheatsheets Rápidos** | [`cheatsheets/`](cheatsheets) | Guias diretos para MCP, RAG, CAG, MAG e Google Gemini Flash. |
| **Laboratórios Práticos** | [`laboratorios/`](laboratorios) | 6 Notebooks interativos passo a passo (Jupyter e ChromaDB). |
| **Projeto Career-AI** | [`src/`](src) | Aplicação integradora em FastAPI com busca semântica de competências. |
| **Slides Animados Mira** | [`slides/`](slides) | Apresentações HTML animadas com coreografia de dados D3.js. |

---

<a id="setup"></a>
## 01 / Prepare e execute a base

```bash
# 1. Clone o repositório
git clone https://github.com/EmmanuelNunes/SECOMP---IA.git
cd SECOMP---IA

# 2. Crie e ative o ambiente virtual
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie o Jupyter Lab para os laboratórios
jupyter lab
```

---

<a id="labs"></a>
## 02 / Arquitetura e fluxo de processamento

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="docs/assets/readme/architecture-still.svg">
  <img src="docs/assets/readme/architecture.svg" alt="Trilha de Laboratórios SECOMP" width="1600" height="520">
</picture>

### Grade de Laboratórios Práticos

| Lab | Tema Principal | Descrição e Entregável | Ambiente |
|:---:|---|---|:---:|
| **Lab 01** | Fundamentos de LLMs & Prompts | Chamadas estruturadas, formatação JSON e mitigação de alucinações. | `Jupyter` |
| **Lab 02** | Embeddings & Busca Vetorial | Representações vetoriais de texto e cálculo de similaridade por cosseno. | `Jupyter` |
| **Lab 03** | RAG Básico (Retrieval-Augmented) | Ingestão com ChromaDB, chunking inteligente e injeção contextual. | `ChromaDB` |
| **Lab 04** | RAG Avançado vs. CAG vs. MAG | Estratégias comparativas de recuperação, re-ranking e janelas expandidas. | `Jupyter` |
| **Lab 05** | Ferramentas & Function Calling | Conexão de agentes a APIs do mundo real e execução controlada. | `Python` |
| **Lab 06** | Agentes Autônomos & ReAct | Implementação de loops perceptivos de decisão e reflexão. | `FastAPI` |

---

<a id="career-ai"></a>
## 03 / Recursos, capacidades e projeto integrador

Localizado em [`src/`](src), o **Career-AI** é a aplicação integradora de demonstração do curso:
- **Backend:** FastAPI assíncrono acoplado ao ChromaDB.
- **Objetivo:** Sistema inteligente de matching e aconselhamento de carreira que analisa currículos e perfis técnicos através de agentes especializados de triagem.

```bash
# Executar o Career-AI
cd src
uvicorn main:app --reload --port 8000
```

---

<a id="structure"></a>
## 04 / Estrutura do repositório

```text
SECOMP---IA/
├── apostila/                # Apostila teórica e conceitual completa
├── cheatsheets/             # Guias de consulta rápida (MCP, RAG, CAG, MAG, Gemini Flash)
├── slides/                  # Apresentações oficiais e templates Mira D3.js
├── datasets/                # Conjuntos de dados (.jsonl) para testes de RAG
├── laboratorios/            # Notebooks práticos (Lab 01 ao Lab 06)
├── src/                     # Código-fonte do projeto integrador Career-AI
├── docs/assets/readme/      # SVGs editoriais de hero e arquitetura
├── AGENTS.md                # Instruções e contratos para agentes de IA
├── CLAUDE.md                # Ponte para Claude Code (@AGENTS.md)
├── README.md                # Documentação em Português (Brasil)
├── README.en.md             # Documentação em Inglês
└── README.es.md             # Documentação em Espanhol
```

---

<a id="research"></a>
## 05 / Referencial metodológico e pesquisa científica

Este workshop e sua esteira didática apoiam-se rigorosamente em publicações científicas e pesquisas contemporâneas em agentes de IA:

### Prof. M.Sc. Sanderson Oliveira de Macedo (Prof. Sandeco)
*Instituto Federal de Goiás (IFG) / Universidade Federal de Goiás (UFG)*
- **Perfil Acadêmico:** [ResearchGate](https://www.researchgate.net/profile/Sanderson-Macedo) | **GitHub Oficial:** [@sandeco](https://github.com/sandeco) | **YouTube:** [Canal Sandeco](https://youtube.com/canalsandeco)
- **Publicações Referenciadas (2026):**
  - *O que faz de um arnês um arnês: condições necessárias e suficientes para um arnês de agente* ([arXiv:2606.10106](https://arxiv.org/abs/2606.10106))
  - *Do Prompt ao Processo: uma Taxonomia de Processos e Avaliação Comparativa de Frameworks de Suporte a Agentes de Desenvolvimento de Software de IA* ([arXiv:2606.04967](https://arxiv.org/abs/2606.04967))
  - *Reversa: Uma estrutura de engenharia de documentação reversa para converter software legado em especificações operacionais para agentes de IA* ([arXiv:2605.18684](https://arxiv.org/abs/2605.18684))

### Prof. Dr. Carlos Alex Sander Juvêncio Gulo
*Universidade do Estado de Mato Grosso (UNEMAT) / Universidade do Porto (FEUP) / Grupo PIXEL*
- Pesquisa de fronteira em inteligência computacional, sistemas distribuídos e visão computacional.

---

<a id="credits"></a>
## 06 / Equipe, condução e licença

- **Instrutor & Organizador:** Emmanuel Nunes
- **Ecossistema:** [EmmanuelNunes/vibe-coding-toolkit](https://github.com/EmmanuelNunes/vibe-coding-toolkit)
- **Licença:** MIT License para código-fonte; materiais textuais sob Creative Commons BY 4.0.

<p align="center">
  <br>
  <strong>BUILD WITH INTENT. SHIP WITH FLOW.</strong>
  <br><br>
  <a href="#workshop-de-ia-e-agentes-autônomos-secomp-2026">Voltar ao topo ↑</a>
</p>
