from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from config import DOCUMENTS_DIR, CHUNK_SIZE

def load_and_split_documents():
    documentos = SimpleDirectoryReader(input_dir=DOCUMENTS_DIR)
    data = documentos.load_data()
    node_parser = SentenceSplitter(chunk_size=CHUNK_SIZE)
    return node_parser.get_nodes_from_documents(data), data
