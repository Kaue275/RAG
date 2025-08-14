import os

PINECONE_API_KEY = os.getenv('pinecone_api')
GROQ_API_KEY = os.getenv('api_rag')

PINECONE_INDEX_NAME = "docs-example"
PINECONE_DIMENSION = 1024
PINECONE_REGION = "us-east-1"

DOCUMENTS_DIR = "documentos"
CHUNK_SIZE = 1024
