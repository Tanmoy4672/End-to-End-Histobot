# HistoBot: A Gen AI Bot for Bangladesh History 
A History Bot designed to receive questions about Bangladesh's history from users and provide detailed, accurate responses based on its knowledge of the subject.
</br></br></br>


## Dataset : 
Here used only 5 books and documentation data written about Bangladesh history:
- Bangladesh Legacy of Blood Anthony Mascarenhas (1986), Reproduced by Sani H. Panhwar (2022)
- A Brief History of Bangladesh With Essays on Bangladesh Studies, Dr. S M A Mamun Chowdhury
- A History of BANGLADESH, Willem van Schendel
- The Bangladesh Reader History, Culture, Politics, Meghna Guhathakurta and Willem van Schendel
- Through Metal Fences: Material Mobility and the Politics of Transnationality at Borders, Malini Sur

## Technologies : 

![Static Badge](https://img.shields.io/badge/huggingface%20-white?style=for-the-badge&logo=huggingface&logoColor=%23FFD21E&labelColor=black&color=black) 
![Static Badge](https://img.shields.io/badge/openai%20-white?style=for-the-badge&logo=openai&logoColor=%23412991&labelColor=black&color=black) 
![Static Badge](https://img.shields.io/badge/langchain%20-white?style=for-the-badge&logo=langchain&logoColor=%231C3C3C&labelColor=black&color=black) 
![Static Badge](https://img.shields.io/badge/pinecone%20-white?style=for-the-badge&labelColor=black&color=black) 
![Static Badge](https://img.shields.io/badge/flask%20-white?style=for-the-badge&logo=flask&logoColor=white&labelColor=black&color=black) 
![Static Badge](https://img.shields.io/badge/html5-black?style=for-the-badge&logo=html5&logoColor=%23E34F26)
![Static Badge](https://img.shields.io/badge/css3-black?style=for-the-badge&logo=css3&logoColor=%231572B6)
![Static Badge](https://img.shields.io/badge/javascript-black?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Static Badge](https://img.shields.io/badge/jquery-black?style=for-the-badge&logo=jquery&logoColor=%230769AD)



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

#### Localhost:8080
>  Histobot appear right corner of the website
<div style="text-align: center;">


|                           |                           |                           |
|---------------------------|---------------------------|---------------------------|
| ![HistoBOT UI 1](https://github.com/Tanmoy4672/End-to-End-Histobot/blob/b032ffef3867aad69f03968987670791e34ff07b/HistoBOT_UI/Screenshot%20from%202025-02-23%2011-30-30.png?width=300) | ![HistoBOT UI 2](https://github.com/Tanmoy4672/End-to-End-Histobot/blob/b032ffef3867aad69f03968987670791e34ff07b/HistoBOT_UI/Screenshot%20from%202025-02-23%2011-31-51.png?width=300) | ![HistoBOT UI 3](https://github.com/Tanmoy4672/End-to-End-Histobot/blob/b032ffef3867aad69f03968987670791e34ff07b/HistoBOT_UI/Screenshot%20from%202025-02-23%2011-32-49.png?width=300) |

</div>






