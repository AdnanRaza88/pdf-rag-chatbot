from fastapi import FastAPI

app = FastAPI(title='PDF RAG Chatbot')

@app.get('/health')
def health():
    return {'status': 'healthy'}
