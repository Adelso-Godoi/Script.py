from flask import Flask, request, jsonify
import config


app = Flask(__name__)

API_KEY = "Senha_ALEaT0ria"


@app.route("/")
def api_():
    return """API para restart do serviço do zimbra Server!
            Siga para o /restart com a chave para execução.    
    """


@app.route("/restart", methods=["POST"])
def rest_():

    token = request.headers.get("Authorization")

    if token != f"Bearer {API_KEY}":
        return "Não autorizado", 401

    retorno = config.restart()

    return jsonify(retorno)


app.run(host="0.0.0.0", port=5000, debug=True)
