# 🎙️ YouTube Transcript Collector (Flask + MongoDB)

Este projeto é uma aplicação web simples em Flask que permite ao usuário inserir o **ID de um vídeo do YouTube** para coletar automaticamente a **transcrição** (legenda automática/manual), **sem precisar da API do Google Cloud**. Os dados são armazenados em um banco de dados **MongoDB** para análise posterior.

---

## 🚀 Funcionalidades

✅ Coleta transcrições de vídeos do YouTube  
✅ Interface web simples usando Flask  
✅ Armazena os dados em MongoDB  
❌ Não utiliza a API oficial do YouTube  
❌ Não coleta comentários, live chats ou superchats (limitação por não usar a API oficial)

---

## 📦 Tecnologias Utilizadas

- Python 3.8+
- Flask
- MongoDB (local ou Atlas)
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)

---

## 🛠️ Instalação

1. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```


3. Certifique-se de que o MongoDB está rodando localmente ou configure sua conexão no arquivo config.py:

python
Copiar
Editar


```python
# config.py
MONGO_URI = 'mongodb://localhost:27017/'
DB_NAME = 'youtube_data'
```

------

## ▶️ Como usar

1. Inicie a aplicação Flask:

```bash
python app.py
```

2. Acesse no navegador:
http://localhost:5000


3. Insira o ID do vídeo do YouTube (por exemplo, para https://www.youtube.com/watch?v=dQw4w9WgXcQ, o ID é dQw4w9WgXcQ)


4. A transcrição será exibida na tela e salva no MongoDB automaticamente.

---------

## 🧪 Exemplo de Documento no MongoDB

A transcrição será salva com o seguinte formato:

```json

{
  "video_id": "dQw4w9WgXcQ",
  "transcript": [
    {
      "text": "Hello, welcome to the video!",
      "start": 0.0,
      "duration": 4.2
    },
    ...
  ]
}

```

-----

### ❗ Limitações

 -  Comentários, live chats e superchats não são acessíveis sem a API oficial do YouTube.

 - Apenas vídeos com transcrição habilitada (manual ou automática) retornarão dados.

------

### 📌 e aqui está o nosso exemplo por um GIF

![GIF de exemplo](assets/arquivo.gif)