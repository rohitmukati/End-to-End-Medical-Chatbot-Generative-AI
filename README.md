
# End-to-End Medical Chatbot
This repository contains an advanced Medical Chatbot built using Generative AI, LangChain, and a Retrieval-Augmented Generation (RAG) pipeline. The chatbot provides accurate and context-aware healthcare responses using a blend of modern AI techniques.

# End-to-end-Medical-Chatbot-Generative-AI


# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/rohitmukati/End-to-End-Medical-Chatbot-Generative-AI
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- GPT
- Pinecone


