from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def get_embedding_model():
    return HuggingFaceEmbedding(model_name="intfloat/multilingual-e5-large")
