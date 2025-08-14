# 🤖 RAG Chatbot com LlamaIndex, Pinecone e Gradio

Este projeto implementa um chatbot baseado em **RAG** (*Retrieval-Augmented Generation*) para responder perguntas a partir de documentos locais (PDFs, textos, etc.), utilizando **LlamaIndex**, **Pinecone** e **Gradio**.

---

## 🚀 Funcionalidades
- Leitura de documentos locais (PDF, TXT, DOCX, etc.).
- Extração e chunking automático do conteúdo para vetorização.
- Armazenamento dos embeddings no **Pinecone**.
- Consulta semântica usando LLMs da **Groq**.
- Interface interativa via **Gradio**.
- Memória de conversa resumida para contexto contínuo.

---
```text
## 📂 Estrutura do Projeto
project/
├── app.py # Ponto de entrada com a interface Gradio
├── config.py # Configurações e variáveis de ambiente
├── data_loader.py # Funções para carregar e processar documentos
├── embedding.py # Criação do modelo de embeddings
├── vector_store.py # Configuração e conexão com Pinecone
├── query_engine.py # Inicialização do Query Engine e Chat Engine
├── memory.py # Configuração de memória do chatbot
├── documentos/ # Pasta para colocar seus PDFs e arquivos de consulta
│ └── exemplo.pdf # Documento de exemplo (dados fictícios)
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo
```
---

## 📥 Como usar

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seuusuario/seuprojeto.git
cd seuprojeto
```

### 2️⃣ Criar e ativar um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variáveis de ambiente
Crie um arquivo .env na raiz do projeto com suas chaves:
```env
pinecone_api=SEU_PINECONE_API_KEY
api_rag=SUA_GROQ_API_KEY
```

### 5️⃣ Adicionar seus documentos
Coloque seus PDFs, TXTs ou outros arquivos na pasta:
```bash
documentos/
```

### 6️⃣ Rodar a aplicação

```bash
python app.py
```

O Gradio abrirá no navegador, permitindo conversar com seu chatbot.

🛠️ Tecnologias Utilizadas
Python 3.10+

LlamaIndex

Pinecone

Gradio

HuggingFace Embeddings

Groq API

