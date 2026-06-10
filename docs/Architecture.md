# Arquitetura do Sistema (Career-AI)

Este documento descreve a arquitetura do nosso Assistente de Carreira Inteligente.

## Componentes Principais

- **Frontend**: Interface para interação do usuário final.
- **Backend**: API Python (FastAPI/Flask) responsável por gerenciar rotas e se comunicar com o modelo de linguagem.
- **RAG Pipeline**: Módulo de *Retrieval-Augmented Generation* que utiliza um banco de dados vetorial para fornecer contexto sobre currículos e mercado de trabalho.
- **Agentes**: Lógica que determina ações autônomas, chamadas a ferramentas externas via MCP (Model Context Protocol).
