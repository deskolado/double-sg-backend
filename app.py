from flask import Flask, jsonify
from model.predictor import gerar_sinal, gerar_sinal_branco

app = Flask(__name__)

@app.route("/sinal")
def sinal():
    resultado = gerar_sinal()
    return jsonify(resultado)

@app.route("/sinal_branco")
def sinal_branco():
    resultado = gerar_sinal_branco()
    return jsonify(resultado)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
