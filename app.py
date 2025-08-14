import gradio as gr
from data_loader import load_and_split_documents
from embedding import get_embedding_model
from vector_store import setup_vector_store
from query_engine import create_query_engine, create_chat_engine

nodes, data = load_and_split_documents()
embed_model = get_embedding_model()
vector_store = setup_vector_store()

query_engine, index, llm = create_query_engine(data, vector_store, embed_model)
chat_engine = create_chat_engine(index, llm)

def responde(message, chat_history):
    if chat_history is None:
        chat_history = []
    response = chat_engine.chat(message)
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": str(response.response)})
    return "", chat_history

def resetar_chat():
    chat_engine.reset()
    return "", []

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type='messages')
    msg = gr.Textbox(label='Digite sua pergunta')
    limpar = gr.Button('Limpar')

    msg.submit(responde, [msg, chatbot], [msg, chatbot])
    limpar.click(resetar_chat, None, [msg, chatbot], queue=False)

if __name__ == '__main__':
  app = create_interface()
  app.launch()
