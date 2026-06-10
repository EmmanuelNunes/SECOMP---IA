# Guia de Instalação

## Pré-Requisitos

- **Python**: Versão 3.11+
  Verifique sua versão rodando:
  ```bash
  python --version
  ```

## Criar Ambiente

Crie um ambiente virtual para isolar as dependências:

```bash
python -m venv .venv
```

**Ativando o ambiente:**

- No **Linux/Mac**:
  ```bash
  source .venv/bin/activate
  ```

- No **Windows**:
  ```powershell
  .venv\Scripts\activate
  ```

## Dependências

Com o ambiente ativado, instale as bibliotecas base:

```bash
pip install langchain langgraph chromadb sentence-transformers fastapi uvicorn
```

## Executar

Para iniciar o servidor FastAPI localmente:

```bash
uvicorn app:app --reload
```
