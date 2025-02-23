from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


# Extract Data from the Pdf
def load_pdf_file(data):
    loader = DirectoryLoader(data, glob = "*.pdf",
                             loader_cls = PyPDFLoader)
    document = loader.load()
    return document 
    
    
# split the data into chunks
def text_split(extracted_data):
    text_spliter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_spliter.split_documents(extracted_data)
    return text_chunks



#download embedding model
def embedding_model():
    model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")        
    return model


