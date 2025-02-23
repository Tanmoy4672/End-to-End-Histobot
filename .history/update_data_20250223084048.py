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

# Assuming extract_pdf_data is already loaded
if extract_pdf_data:
    num_rows = len(extract_pdf_data)
    print(f"Number of rows (documents) created: {num_rows}")
else:
    print("No data found in 'extract_pdf_data'.")
    
    

