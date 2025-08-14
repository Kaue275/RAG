from llama_index.core import VectorStoreIndex
from llama_index.llms.groq import Groq
from config import GROQ_API_KEY
from memory import get_memory

def create_query_engine(data, vector_store, embed_model):
    storage_context = vector_store
    index = VectorStoreIndex.from_documents(data, storage_context=storage_context, embed_model=embed_model)
    llm = Groq(model='llama-3.3-70b-versatile', api_key=GROQ_API_KEY)
    return index.as_query_engine(similarity_top_k=2, llm=llm), index, llm

def create_chat_engine(index, llm):
    return index.as_chat_engine(
        chat_mode='context',
        llm=llm,
        memory=get_memory(llm),
        system_prompt=('Você é um especialista em computadores e jogos...')
    )
