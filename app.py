from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

API_ENDPOINT = 'https://wizard-world-api.herokuapp.com/Elixirs'

@app.route('/', methods=['GET', 'POST'])
def render_potion():
    

    if request.method == 'POST':
        try:
            response = requests.get(API_ENDPOINT) 
            if response.status_code == 200:
                dados = response.json()
                if dados: 
                    pocao_aleatoria = random.choice(dados)
                    nome_pocao = pocao_aleatoria.get('name', 'Poção Desconhecida')
                    efeito_pocao = pocao_aleatoria.get('effect', 'Efeito desconhecido')
                    characteristics = pocao_aleatoria.get('characteristics',False)
                    time = pocao_aleatoria.get('time',False)
                    difficulty = pocao_aleatoria.get('difficulty',False)
                    
                    return render_template('index.html', nome=nome_pocao, efeito=efeito_pocao, characteristics=characteristics,time=time, difficulty=difficulty)
                    
                else:
                    erro = "Nenhuma poção encontrada na API!"
            else:
                erro = f"Erro na API: {response.status_code}"
        except requests.exceptions.RequestException as erro:
            erro = f"Erro ao conectar com a API"
        return render_template('index.html', erro=erro)
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
