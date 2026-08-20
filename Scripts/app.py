#from flask import Flask

#app = Flask(__name__)


#@app.route("/")
#def inicio():
    #return "Minha primeira API"
 #   return "Testando frase na API"

#app.run(debug=True)

from flask import Flask, jsonify

app = Flask(__name__)

# Simulando um "banco de dados" com um dicionário Python
produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 150.00},
    {"id": 2, "nome": "Mouse Gamer", "preco": 80.00},
    {"id": 3, "nome": "Monitor 144Hz", "preco": 900.00}
]

@app.route("/")
def inicio():
    return "Bem-vindo à minha API de produtos! Acesse /produtos para ver a lista."

# Nova "rota" que disponibiliza as informações
@app.route("/produtos")
def obter_produtos():
    # O jsonify transforma nosso dicionário/lista Python em JSON
    return jsonify(produtos)

if __name__ == "__main__":
    app.run(debug=True)