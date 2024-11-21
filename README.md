
# End-to-End Medical Chatbot
This repository contains an advanced Medical Chatbot built using Generative AI, LangChain, and a Retrieval-Augmented Generation (RAG) pipeline. The chatbot provides accurate and context-aware healthcare responses using a blend of modern AI techniques.

Features
PDF Support: Extracts information from medical documents using PyPDF loader.
Data Chunking: Processes and splits extracted content into manageable chunks for efficient embedding.
Embedding Creation: Uses a Hugging Face embedding model to convert text into high-dimensional vectors.
Vector Database: Implements Pinecone Vector Database to store and manage embeddings efficiently.
RAG Pipeline: Combines retrieval and generation using OpenAI's LLM model for enhanced query understanding and response generation.
Contextual Medical Assistance: Delivers precise responses to user queries based on document embeddings and real-time language understanding.

################################################################################################################################################################
Workflow
PDF Parsing: Documents are loaded and parsed using PyPDF.
Chunking: Parsed content is split into smaller, meaningful text chunks.
Embedding Generation: Chunks are converted into embeddings using Hugging Face models.
Vector Indexing: Embeddings are stored in a Pinecone vector database, with indices created and managed for retrieval.
Retrieval & Augmented Generation: The RAG pipeline fetches relevant embeddings and passes them to OpenAI's LLM for generating user responses.

################################################################################################################################################################
Tech Stack
LangChain: Framework for building language model applications.
Generative AI: Powered by OpenAI's language models.
PyPDF Loader: For PDF parsing and content extraction.
Hugging Face: For generating embeddings from text data.
Pinecone: Vector database for storing and querying embeddings.
RAG Pipeline: For combining retrieval with generative AI.

#################################################################################################################################################################
Setup Instructions
Clone the repository.
git clone https://github.com/rohitmukati/End-to-End-Medical-Chatbot-Generative-AI

Install dependencies:
pip install -r requirements.txt  

##################################################################################################################################################################
Add your OpenAI API key and Pinecone credentials to the environment variables.

Run the application:
python app.py  
Future Enhancements
Support for additional file formats (e.g., Word, Excel).
Integration with more vector databases.
Multilingual support for broader accessibility.
License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! Feel free to submit issues or pull requests for new features and improvements.

