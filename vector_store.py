from pinecone import Pinecone, ServerlessSpec
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import StorageContext
from config import PINECONE_API_KEY, PINECONE_INDEX_NAME, PINECONE_DIMENSION, PINECONE_REGION

def setup_vector_store():
    pc = Pinecone(api_key=PINECONE_API_KEY)
    
    pc.delete_index(PINECONE_INDEX_NAME)
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=PINECONE_DIMENSION,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region=PINECONE_REGION)
    )

    pinecone_index = pc.Index(PINECONE_INDEX_NAME)
    return PineconeVectorStore(pinecone_index=pinecone_index)
