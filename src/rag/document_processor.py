import json

def load_jsonl(filepath):
    """Carrega dados mockados de um arquivo JSONL."""
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data

def chunk_text(text, chunk_size=500, overlap=50):
    """
    Quebra um texto maior em pedaços menores (chunks) para facilitar a 
    busca e melhorar o contexto passado para o modelo.
    """
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i+chunk_size])
    return chunks
