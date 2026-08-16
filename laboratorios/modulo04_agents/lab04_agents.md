# Laboratório 04: Construindo Agentes Autônomos & Orquestração Agêntica

## 🎯 Objetivo
Criar agentes autônomos com ciclos de raciocínio ReAct, chamadas a ferramentas e compreender os padrões de orquestração do **Google Antigravity (AGY)** e **Agent Harnesses**.

---

## 🏛️ Arquitetura do Ciclo Agêntico

O fluxo de execução ReAct opera no seguinte ciclo recursivo:
```text
Usuário (Meta) ──> Agente (Raciocínio / ReAct) ──> Tool Calling (MCP / Funções)
                         │                                 │
                         ▼                                 ▼
                 Resposta Final <────────────── Retorno da Execução
```

---

## 🧪 Exercício 1: Agente Gerador de Documentação (DocAgent)
**Objetivo:** Construir um agente capaz de inspecionar a árvore de arquivos de um projeto e gerar um `README.md` automaticamente.

**Plano de Execução:**
1. Listar arquivos do repositório (`list_dir` / `os.listdir`);
2. Ler os principais scripts Python (`view_file` / `open()`);
3. Identificar dependências e funções expostas;
4. Sintetizar um README estruturado em Markdown com badges e exemplos de uso;
5. Salvar o arquivo no disco.

---

## 🧪 Exercício 2: ResearchAgent com Ferramentas de Busca
Construa um agente de pesquisa acadêmica capaz de:
- Consultar fontes científicas (ex: arXiv);
- Extrair citações e resumos de artigos;
- Estruturar um estado compartilhado no LangGraph.

---

## 🤖 Exercício 3: Padrões de Subagentes no Google Antigravity
No ambiente **Google Antigravity**, múltiplos subagentes podem ser orquestrados para dividir tarefas pesadas:
- **Subagente de Pesquisa (`research`):** Explora a base de código em modo leitura.
- **Subagente de Execução (`self` / `worker`):** Aplica mudanças em um workspace isolado (`branch`).
- **Comunicação:** Troca assíncrona de mensagens sem necessidade de loops bloqueantes.
