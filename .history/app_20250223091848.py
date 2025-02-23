from flask import flask, render_template, jsonify, request
from src.helper import load_pdf_file, text_split, embedding_model
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = flask(__name__)


load_dotenv()

#Pinecone API
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

#OpenAI API
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

embeddings = embedding_model()

index_name = "histobot"


docusearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
retrieved_docs = retriever.invoke("when did the first SAARC summit held in Dhaka?")
llm = OpenAI(temperature=0.4, max_tokens=500)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", System),
        ("human", "{input}"),
    ]
)

question_answering_chain = create_stuff_documents_chain(llm, prompt_template)
rag_chain = create_retrieval_chain(retriever, question_answering_chain)


@app.route("/")
def index():
    return render__template('index.html')

@app.route("/get", methods=["GET", "POST"])