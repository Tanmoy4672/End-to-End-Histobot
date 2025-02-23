from flask import Flask, render_template, jsonify, request
from src.helper import load_pdf_file, text_split, embedding_model
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)


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

retriever = docusearch.as_retriever(search_type="similarity", search_kwargs={"k":3})
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
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form.g["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": input})
    print("Response :", response["answer"])
    return str(response["answer"])

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8080, debug=True)
