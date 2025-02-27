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

# Pinecone API
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
if not PINECONE_API_KEY:
    raise ValueError("PINECONE_API_KEY not found in .env file")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# OpenAI API
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

embeddings = embedding_model()

index_name = "histobot"

try:
    docusearch = PineconeVectorStore.from_existing_index(
        index_name=index_name,
        embedding=embeddings
    )
except Exception as e:
    print("Error connecting to Pinecone:", e)
    raise

retriever = docusearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

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

@app.route("/get", methods=["POST"])
def chat():
    if request.method == "POST":
        try:
            data = request.json
            msg = data.get("message")
            if not msg:
                return jsonify({"error": "No message provided"}), 400
            print("User Input:", msg)
            response = rag_chain.invoke({"input": msg})
            print("Full Response:", response)
            if "answer" in response:
                return jsonify({"response": response["answer"]})
            else:
                return jsonify({"response": "Sorry, I couldn’t find an answer. Please try again with a different question."}), 500
        except Exception as e:
            print("Error in chat:", str(e))
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "Method not allowed"}), 405

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)