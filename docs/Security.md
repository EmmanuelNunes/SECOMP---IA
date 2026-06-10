# Segurança em IA

Diretrizes de segurança para a construção do Career-AI:

1. **Proteção contra Prompt Injection**: Sanitização das entradas fornecidas pelos usuários para que não sobrescrevam as instruções do sistema.
2. **Segredos e Credenciais**: Chaves de API (`OPENAI_API_KEY`, etc) devem ficar EXCLUSIVAMENTE em arquivos `.env`, que nunca serão commitados.
3. **Escopo de Execução (MCP)**: Agentes que rodam código ou acessam arquivos devem operar em modo *sandboxed* (restrito) e pedir permissão explícita para ações sensíveis.
