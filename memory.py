from llama_index.core.memory import ChatSummaryMemoryBuffer

def get_memory(llm):
    return ChatSummaryMemoryBuffer(llm=llm, token_limit=500)
