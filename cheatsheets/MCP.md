# Entregável 5: Cheat Sheet MCP (Model Context Protocol)

O **Model Context Protocol (MCP)** padroniza como modelos de IA se comunicam com fontes de dados e ferramentas externas.

## Arquitetura
`CLIENT` (LLM/Agente) <---> `MCP` <---> `SERVER` (Ferramenta Local/API)

## Principais Componentes

1. **Tool (Ferramenta):** Ações executáveis que o LLM pode pedir para o servidor rodar (ex: rodar um script, fazer um commit).
2. **Resource (Recurso):** Dados estáticos ou dinâmicos que o servidor expõe para o LLM ler (ex: arquivos locais, logs).
3. **Prompt:** Modelos de instruções ou fluxos de conversação definidos no servidor.

## Fluxo Típico

1. **Agent** (Cliente) decide que precisa de contexto ou quer executar uma ação.
2. Comunica-se via **MCP** com um servidor local/remoto.
3. O Servidor MCP atua como ponte e interage com **GitHub**, **Filesystem (Sistema de Arquivos)**, **Databases**, etc.
4. O servidor devolve os dados/resultado para o Agente.
