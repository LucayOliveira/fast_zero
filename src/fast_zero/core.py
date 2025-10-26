from fastapi import FastAPI
from fast_zero.schemas import Message
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', response_model = Message)
def read_root():
    return {'Message': 'Hello World'}

@app.get('/html', response_class = HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <title>Página Olá mundo</title>
        <meta charset="utf-8">
    </head>
    <body>
        Olá Mundo
    </body>
    </html>"""
