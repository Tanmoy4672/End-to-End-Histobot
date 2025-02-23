from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings


# Extract Data from the Pdf
def load_pdf_file(data):
    loader = DirectoryLoader(data, glob = "*.pdf",
                             loader_cls = PyPDFLoader)
    document = loader.load()
    return document 



# Assuming extract_pdf_data is already loaded
if extract_pdf_data:
    num_rows = len(extract_pdf_data)
    print(f"Number of rows (documents) created: {num_rows}")
else:
    print("No data found in 'extract_pdf_data'.")
    
    
    
