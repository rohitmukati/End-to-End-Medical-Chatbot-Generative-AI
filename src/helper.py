from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings





def load_pdf_files():
    loader = PyPDFLoader("Data\Medical_book.pdf")
    documents = loader.load()
    
    return documents



## Splitting data into chunks

def text_splitter(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=20 )
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks


## download the embedding from huggingface

def download_huggingface_embedding():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings
    
    






























