from src.helper import load_pdf_file, text_split, embedding_model
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os


load_dotenv()
