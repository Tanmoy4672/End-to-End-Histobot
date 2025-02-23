from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


# Extract Data from the Pdf
def load_pdf_file(data):
    loader = DirectoryLoader(data, glob = "*.pdf",
                             loader_cls = PyPDFLoader)
    document = loader.load()
    return document 

