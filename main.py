book = ""

import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

model = init_chat_model(model="gpt-4o")

from langchain_openai import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")

from langchain_core.vectorstores import InMemoryVectorStore

vector_store = InMemoryVectorStore(embeddings_model)

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

splits = text_splitter.split_text(book)

vector_store.add_texts(splits)

query = "What is the best way for me to make a new habit in the morning?"
results = vector_store.similarity_search(query, k=1)

for i, doc in enumerate(results, 1):
    print(model.invoke("Answer the question: " + query + " By using direct quotes from the following excerpt from the book extensively:" + doc.page_content).content)
