import os
import streamlit as st
from dotenv import load_dotenv

# Cloud-specific Imports
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, Settings
from llama_index.llms.groq import Groq
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.vector_stores.pinecone import PineconeVectorStore
from pinecone import Pinecone
from google.genai.types import EmbedContentConfig

# 1. Load Keys
load_dotenv()

# 2. Configuration (RAM-Optimized Cloud Settings)
# BRAIN: Groq (Free)
Settings.llm = Groq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

# EYES: Gemini (Free) - Ensure you use 'models/embedding-001'
Settings.embed_model = GoogleGenAIEmbedding(
    model_name="models/gemini-embedding-001",
    api_key=os.getenv("GOOGLE_API_KEY"),
    embedding_config=EmbedContentConfig(output_dimensionality=2048) # FORCED 2048
)

# 3. Connect to Pinecone (Cloud Memory)
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
# Replace "your-index-name" with the exact name of the index you created in Pinecone
# Dimensions must be 768 for Gemini embedding-001
pinecone_index = pc.Index("rag-index", dimension=2048) 

# Link Pinecone to LlamaIndex
vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 4. Streamlit UI
st.title("RAG project on KarunAI")
st.sidebar.success("Mode: All-Cloud (RAM Safe)")

if "messages" not in st.session_state:
    st.session_state.messages = []

@st.cache_resource(show_spinner=False)
def initialize_cloud_index():
    if not os.path.exists("./data") or not os.listdir("./data"):
        st.error("Please add files to the 'data' folder.")
        return None
    
    # Load and upload to Pinecone
    documents = SimpleDirectoryReader("./data").load_data()
    # from_documents handles the embedding and the cloud upload automatically
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context
    )
    return index

index = initialize_cloud_index()

if index:
    chat_engine = index.as_chat_engine(chat_mode="context", streaming=True)

    # Chat UI Loop
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask about your cloud-indexed documents"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response_stream = chat_engine.stream_chat(prompt)
            response_text = st.write_stream(response_stream.response_gen)
        
        st.session_state.messages.append({"role": "assistant", "content": response_text})