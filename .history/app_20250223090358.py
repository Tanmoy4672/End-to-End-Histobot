from flask import flask, render_template, jsonify, request
from src.helper import load_pdf_file, text_split, embedding_model
from langchain import l