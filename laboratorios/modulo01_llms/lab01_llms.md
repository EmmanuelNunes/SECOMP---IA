# Laboratório 01: Introdução aos LLMs & Raciocínio Híbrido com Gemini 3.7 Flash

## 🎯 Objetivo
Compreender o funcionamento de Grandes Modelos de Linguagem e experimentar o **Raciocínio Híbrido (*Hybrid Reasoning*)** do modelo vigente **Gemini 3.7 Flash**.

---

## 🧪 Exercício 1: Impacto do Prompt no Processamento do LLM
Teste o seguinte prompt básico:
> *"Explique o que é Inteligência Artificial em 100 palavras."*

Em seguida, altere para um prompt com persona e público-alvo definidos:
> *"Você é um professor de Ciência da Computação. Explique o que é Inteligência Artificial para um calouro do curso utilizando analogias de software."*

**Observe na nova resposta:**
- O tom e rigor conceitual;
- A estruturação das analogias;
- A precisão técnica.

---

## 🧪 Exercício 2: Engenharia de Contexto
Compare a resposta do prompt curto e isolado:
> *"O que é RAG?"*

Com a resposta deste prompt contextualizado:
> *"Explique RAG (Retrieval-Augmented Generation) comparando-o com CAG (Cache-Augmented Generation) e MAG (Memory-Augmented Generation), destacando latência e casos de uso."*

---

## 🧠 Exercício 3: Test-Time Compute no Gemini 3.7 Flash (Standard vs. Thinking Mode)

O **Gemini 3.7 Flash** permite regular o orçamento de pensamento (*Thinking Budget*).

### Caso A: Modo Padrão (Sem Thinking / Resposta Imediata)
Envie uma pergunta direta de código:
```python
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents="Escreva uma função em Python para calcular o n-ésimo número de Fibonacci em tempo linear O(n) e espaço O(1)."
)
print(response.text)
```
*Observe a resposta quase instantânea com altíssima taxa de geração de tokens.*

### Caso B: Modo de Pensamento (Thinking Mode Ativado)
Agora solicite a resolução e prova de um problema de concorrência ou arquitetura distribuída:
```python
response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents="Projete uma arquitetura tolerante a falhas para processamento de eventos de IA em tempo real com garantia Exactly-Once em Python. Analise race conditions e prove a corretude do algoritmo."
)
print(response.text)
```
*Observe o processo de raciocínio profundo (*Chain-of-Thought*) expandido internamente para entregar uma solução completa e à prova de falhas.*
