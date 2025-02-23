from src.helper import load_pdf_file, text_split, embedding_model
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

#Pinecone API
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


extract_pdf_data = load_pdf_file(data = "Dataset/")
text_chunks = text_split(extract_pdf_data)
embeddings = embedding_model()

pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "histobot"

pc.upsert(
    name = index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)


document_upsert = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name="histobot",
    embedding=embeddings,
)