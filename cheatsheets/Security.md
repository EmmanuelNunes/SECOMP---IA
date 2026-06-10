# Entregável 7: Cheat Sheet Segurança em IA

## Vulnerabilidades e Ameaças Comuns

- **Prompt Injection**: Injeção de texto pelo usuário com o objetivo de alterar o comportamento ou a instrução original do sistema.
  - *Mitigação*: Uso de **Sanitização** nas entradas e separação clara entre as instruções do sistema e o conteúdo do usuário.

- **Jailbreak**: Conjunto de técnicas focadas em burlar as diretrizes éticas e filtros de segurança do modelo de IA.
  - *Mitigação*: Implementação de **Guardrails** (barreiras de proteção que filtram tanto as entradas quanto as respostas do LLM).

- **Data Leakage (Vazamento de Dados)**: Risco de o modelo expor informações sigilosas acidentalmente a partir da sua base de RAG ou treinamento.
  - *Mitigação*: Forte **Controle de Acesso** aos documentos e bases de dados consultadas pelo sistema.

- **Excessive Agency (Agência Excessiva)**: Quando um agente inteligente ganha autonomia e ferramentas com poder exagerado (ex: deletar banco de dados, enviar e-mails em massa).
  - *Mitigação*: Implementar **RBAC** (Role-Based Access Control) e manter um humano no fluxo (*Human in the Loop*) para aprovações críticas.

---

## Checklist de Produção (Go-Live)

- [ ] **Logs**: O sistema registra adequadamente as interações para detecção de anomalias?
- [ ] **Auditoria**: Há rastreabilidade para todas as ações executadas pelos agentes (Tools MCP)?
- [ ] **Criptografia**: Os dados dos usuários, chaves de API e bases do Vector DB estão criptografados?
- [ ] **LGPD**: A aplicação respeita a coleta mínima e diretrizes de privacidade dos usuários?
- [ ] **Menor Privilégio**: O servidor MCP foi configurado dando estritamente o acesso mínimo necessário para o Agente operar?
