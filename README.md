# 🤖 AI Document Analyser using RAG

A cloud-based AI document analysis application built using **Retrieval Augmented Generation (RAG)**.  
The application allows users to upload documents and interact with them using natural language queries.

The system uses LLMs, embeddings, and vector databases to retrieve relevant document information and generate accurate AI responses.

---

# 🚀 Features

- 📄 Document-based question answering
- 🤖 AI chatbot for uploaded documents
- 🔍 Semantic search using embeddings
- 🧠 Retrieval Augmented Generation (RAG) pipeline
- ☁️ Fully cloud-based architecture
- ⚡ Optimized for low RAM usage
- 💬 Interactive Streamlit chat interface

---

# 🏗️ Architecture

The project follows a RAG workflow:
Document
|
↓
Document Loader
(SimpleDirectoryReader)
|
↓
Text Embeddings
(Google Gemini Embedding Model)
|
↓
Vector Database
(Pinecone)
|
↓
User Query
|
↓
Similarity Search
|
↓
LLM Generation
(Groq Llama 3.3)
|
↓
AI Response


---

# 🛠️ Tech Stack

## Frontend

- Streamlit

## AI / LLM

- Groq API
- Llama 3.3 70B Versatile

## Embeddings

- Google Gemini Embedding Model

## Vector Database

- Pinecone

## Framework

- LlamaIndex

---

# 📂 Project Structure


ai_doc_analyser/

│
├── app.py
│
├── data/
│ └── sample.txt
│
├── .env
│
├── requirements.txt
│
└── README.md


---

# 🔑 Environment Variables

Create a `.env` file:

.env
GROQ_API_KEY=your_groq_api_key

GOOGLE_API_KEY=your_google_api_key

PINECONE_API_KEY=your_pinecone_api_key
⚙️ Installation

Clone the repository:

git clone https://github.com/SSrushti-s/ai_doc_analyser.git

Move into the project folder:

cd ai_doc_analyser

Create virtual environment:

python -m venv venv

Activate environment:

Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
▶️ Run Application

Start Streamlit:

streamlit run app.py

The application will open at:

http://localhost:8501
🧠 How It Works
Documents are loaded from the data folder.
LlamaIndex processes the document content.
Gemini creates vector embeddings.
Embeddings are stored in Pinecone.
User questions are converted into embeddings.
Pinecone retrieves relevant document chunks.
Groq Llama model generates the final response.
📌 Current Limitation

Currently the project uses a small sample document (sample.txt) for faster loading and testing.

Large documents may take longer because:

Document processing requires generating embeddings.
Data needs to be uploaded and indexed in Pinecone.

Future improvements:

Background document processing
Support for multiple file formats
Document upload UI
Persistent indexing
Chat history storage
🌟 Future Enhancements
📚 Support PDF, DOCX, and multiple documents
🔐 User authentication
🗂️ Separate vector indexes per user
💾 Persistent conversation memory
🚀 Deployment on cloud platforms
