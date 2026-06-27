from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "partidas.json")


def carregar_partidas():
    with open(DATA_FILE, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "nome": "API de Jogos Multiplayer",
        "versao": "1.0.0",
        "status": "online"
    }), 200


@app.route("/partidas", methods=["GET"])
def listar_partidas():
    try:
        partidas = carregar_partidas()

        return jsonify({
            "status": "sucesso",
            "quantidade": len(partidas),
            "dados": partidas
        }), 200

    except Exception as erro:
        return jsonify({
            "status": "erro",
            "mensagem": "Erro interno ao listar partidas",
            "detalhe": str(erro)
        }), 500


@app.route("/partidas/<int:id>", methods=["GET"])
def buscar_partida_por_id(id):
    try:
        partidas = carregar_partidas()

        for partida in partidas:
            if partida["id"] == id:
                return jsonify({
                    "status": "sucesso",
                    "dados": partida
                }), 200

        return jsonify({
            "status": "erro",
            "mensagem": "Partida nao encontrada"
        }), 404

    except Exception as erro:
        return jsonify({
            "status": "erro",
            "mensagem": "Erro interno ao buscar partida",
            "detalhe": str(erro)
        }), 500


@app.errorhandler(404)
def rota_nao_encontrada(error):
    return jsonify({
        "status": "erro",
        "mensagem": "Rota não encontrada"
    }), 404


@app.errorhandler(500)
def erro_interno(error):
    return jsonify({
        "status": "erro",
        "mensagem": "Erro interno do servidor"
    }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
