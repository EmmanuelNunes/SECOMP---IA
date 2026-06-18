import os
import sys
import json

# Adiciona o diretório-raiz do projeto ao sys.path para permitir imports absolutos
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.rag.vector_store import VectorStore
from src.rag.document_processor import load_jsonl

def ingest_all_datasets():
    """Lê os arquivos JSONL do diretório de datasets e realiza a ingestão no ChromaDB."""
    db_path = os.path.join(project_root, "chroma_db")
    vector_store = VectorStore(db_path=db_path)
    
    datasets_dir = os.path.join(project_root, "datasets")
    
    # 1. Ingestão de Currículos
    resumes_path = os.path.join(datasets_dir, "resumes.jsonl")
    if os.path.exists(resumes_path):
        resumes = load_jsonl(resumes_path)
        docs = []
        metadatas = []
        ids = []
        for r in resumes:
            doc_content = f"Candidato(a) {r['name']} possui as seguintes habilidades técnicas: {', '.join(r['skills'])}. Tempo de experiência: {r['experience_years']} anos."
            docs.append(doc_content)
            metadatas.append({
                "type": "resume",
                "candidate_id": r["candidate_id"],
                "name": r["name"]
            })
            ids.append(f"resume_{r['candidate_id']}")
        vector_store.add_documents(docs, metadatas, ids)
        print(f"Ingestão concluída para {len(docs)} currículos.")

    # 2. Ingestão de Perguntas de Entrevistas
    questions_path = os.path.join(datasets_dir, "interview_questions.jsonl")
    if os.path.exists(questions_path):
        questions = load_jsonl(questions_path)
        docs = []
        metadatas = []
        ids = []
        for idx, q in enumerate(questions):
            doc_content = f"Pergunta para simulação de entrevista técnica: '{q['question']}'. Resposta sugerida esperada: {q['answer']}."
            docs.append(doc_content)
            metadatas.append({
                "type": "interview_question",
                "index": idx
            })
            ids.append(f"question_{idx}")
        vector_store.add_documents(docs, metadatas, ids)
        print(f"Ingestão concluída para {len(docs)} perguntas de entrevista.")

    # 3. Ingestão de Roteiros de Estudo (Study Guides)
    guides_path = os.path.join(datasets_dir, "study_guides.jsonl")
    if os.path.exists(guides_path):
        guides = load_jsonl(guides_path)
        docs = []
        metadatas = []
        ids = []
        for idx, g in enumerate(guides):
            doc_content = f"Tópico de Estudo: {g['topic']}. Resumo da tecnologia: {g['summary']}. Conceitos-chave abordados: {', '.join(g['key_concepts'])}."
            docs.append(doc_content)
            metadatas.append({
                "type": "study_guide",
                "topic": g["topic"]
            })
            ids.append(f"guide_{idx}")
        vector_store.add_documents(docs, metadatas, ids)
        print(f"Ingestão concluída para {len(docs)} roteiros de estudo.")

    print("--- Processo de Ingestão Finalizado no ChromaDB ---")

if __name__ == "__main__":
    ingest_all_datasets()
