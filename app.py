from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

API_ENDPOINT = 'https://wizard-world-api.herokuapp.com/Elixirs'

@app.route('/', methods=['GET', 'POST'])
def render_potion():
    nome_pocao = None
    efeito_pocao = None
    erro = None

    if request.method == 'POST':
        try:
            response = requests.get(API_ENDPOINT) 
            if response.status_code == 200:
                dados = response.json()
                if dados: 
                    pocao_aleatoria = random.choice(dados)
                    nome_pocao = pocao_aleatoria.get('name', 'Poção Desconhecida')
                    efeito_pocao = pocao_aleatoria.get('effect', 'Efeito desconhecido')
                else:
                    erro = "Nenhuma poção encontrada na API!"
            else:
                erro = f"Erro na API: {response.status_code}"
        except requests.exceptions.RequestException as e:
            erro = f"Erro ao conectar com a API"

    return render_template('index.html', nome=nome_pocao, efeito=efeito_pocao, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
