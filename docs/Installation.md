# Guia de Instalação e Configuração do Ambiente

Este guia descreve os passos para configurar o ambiente de desenvolvimento do workshop da **SECOMP 2026**, incluindo as bibliotecas Python, a chave do modelo vigente **Gemini 3.7 Flash** e a plataforma **Google Antigravity (AGY)**.

---

## 📋 Pré-Requisitos

- **Python**: Versão 3.11 ou superior
  ```bash
  python --version
  ```
- **Git**: Instalado e configurado no terminal
- **Google AI Studio API Key**: Para acesso aos modelos Gemini

---

## 🐍 1. Criar e Ativar Ambiente Virtual Python

Crie um ambiente virtual para isolar as dependências:

```bash
python -m venv .venv
```

**Ativando o ambiente:**

- No **Linux/macOS**:
  ```bash
  source .venv/bin/activate
  ```

- No **Windows (PowerShell)**:
  ```powershell
  .venv\Scripts\activate
  ```

---

## 📦 2. Instalar Dependências

Com o ambiente ativado, instale as bibliotecas base do workshop:

```bash
pip install langchain langgraph chromadb sentence-transformers fastapi uvicorn google-genai pydantic
```

---

## 🔑 3. Configurar Chave da API do Gemini (Gemini 3.7 Flash)

Obtenha sua chave gratuita ou enterprise no [Google AI Studio](https://aistudio.google.com/) e configure a variável de ambiente:

- No **Linux/macOS**:
  ```bash
  export GEMINI_API_KEY="sua-chave-aqui"
  ```

- No **Windows (PowerShell)**:
  ```powershell
  $env:GEMINI_API_KEY="sua-chave-aqui"
  ```

---

## 🤖 4. Plataforma de Desenvolvimento: Google Antigravity (AGY)

O **Google Antigravity** é o ambiente oficial de desenvolvimento agêntico utilizado no workshop.

```bash
# Iniciar sessão do Antigravity CLI no projeto
agy

# Executar especificando o modelo Gemini 3.7 Flash
agy --model gemini-3.7-flash
```

---

## 🚀 5. Executar o Backend do Career-AI

Para iniciar o servidor FastAPI do projeto integrador localmente:

```bash
uvicorn app:app --reload
```
Acesse a documentação interativa da API em: `http://localhost:8000/docs`.
