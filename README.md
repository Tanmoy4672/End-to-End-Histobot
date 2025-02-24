# End-to-End-HistoBot: A Gen AI Bot for Bangladesh History 

A History Bot designed to receive questions about Bangladesh's history from users and provide detailed, accurate responses based on its knowledge of the subject.

## Technologies : 

![Static Badge](https://img.shields.io/badge/huggingface%20-white?style=for-the-badge&logo=huggingface&logoColor=%23FFD21E&labelColor=black&color=black) 
![Static Badge](https://img.shields.io/badge/openai%20-white?style=for-the-badge&logo=openai&logoColor=%23412991&labelColor=black&color=black) 
![Static Badge](https://img.shields.io/badge/langchain%20-white?style=for-the-badge&logo=langchain&logoColor=%231C3C3C&labelColor=black&color=black) 
![Static Badge](https://img.shields.io/badge/pinecone%20-white?style=for-the-badge&labelColor=black&color=black) 
![Static Badge](https://img.shields.io/badge/flask%20-white?style=for-the-badge&logo=flask&logoColor=white&labelColor=black&color=black) 

## How to Run : 

>  Active Conda environment (Windows)
```bash
conda create -n Histobot python=3.10 -y
```
```bash
conda active Histobot
```
>  Active Conda environment (Linux/Ubuntu)
```bash
source venv/bin/activate
```
>  Install all the requirements 
```bash
conda create n Histobot python=3.10 -y
```
>  Install all the requirements 
```bash
pip install -r requirements.txt
```

#### Create API-KEY
>  Create Pinecone & OpenAI API-KEY. Keep it in ⚙️.env file 
```bash
PINECONE_API_KEY = "PINECONE-API-KEY"
OPENAI_API_KEY = "OPENAI-API-KEY"
```

>  Run [app.py](app.py)
```bash
python app.py
```




