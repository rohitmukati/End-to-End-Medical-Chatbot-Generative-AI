from src.helper import load_pdf_files, text_splitter, download_huggingface_embedding
from pinecone import ServerlessSpec
from pinecone.grpc import PineconeGRPC as Pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os


load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

extracted_data = load_pdf_files()
text_chunk = text_splitter(extracted_data)
embedding = download_huggingface_embedding()


## pinecone inilization
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medicalbot"

pc.create_index(
    name=index_name,
    dimension=384, # Replace with your model dimensions
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)


## embedded each quey and chunk into pinecone VectorStores
docssearch = PineconeVectorStore.from_documents(
    documents=text_chunk,
    index_name=index_name,
    embedding=embedding
)





















