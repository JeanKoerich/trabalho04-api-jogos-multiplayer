import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


@pytest.fixture
def cliente():
    app.config["TESTING"] = True

    with app.test_client() as cliente_teste:
        yield cliente_teste


def test_listar_partidas_retorna_200(cliente):
    resposta = cliente.get("/partidas")

    assert resposta.status_code == 200


def test_listar_partidas_tem_estrutura_json(cliente):
    resposta = cliente.get("/partidas")
    dados = resposta.get_json()

    assert "status" in dados
    assert "quantidade" in dados
    assert "dados" in dados
    assert isinstance(dados["dados"], list)
    assert len(dados["dados"]) >= 10

    primeira_partida = dados["dados"][0]

    assert "id" in primeira_partida
    assert "jogador1" in primeira_partida
    assert "jogador2" in primeira_partida
    assert "pontos_jogador1" in primeira_partida
    assert "pontos_jogador2" in primeira_partida
    assert "status" in primeira_partida


def test_buscar_partida_inexistente_retorna_404(cliente):
    resposta = cliente.get("/partidas/999")

    assert resposta.status_code == 404


def test_status_da_api_retorna_online(cliente):
    resposta = cliente.get("/status")
    dados = resposta.get_json()

    assert resposta.status_code == 200
    assert dados["nome"] == "API de Jogos Multiplayer"
    assert dados["versao"] == "1.0.0"
    assert dados["status"] == "online"