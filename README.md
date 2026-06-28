# API REST para Servidor de Jogos Multiplayer

Este projeto foi desenvolvido para o Trabalho Final da disciplina de Cloud Computing. O objetivo foi criar uma API REST simples, mantendo relação com os trabalhos anteriores da disciplina, que tinham como tema aplicações e servidores de jogos multiplayer.

A API permite consultar o status da aplicação, listar partidas multiplayer simuladas e buscar uma partida específica pelo identificador. Os dados são carregados a partir de um arquivo JSON externo, evitando que os registros fiquem fixos diretamente no código.

### Objetivo do projeto

O objetivo principal do projeto é demonstrar a criação de uma API REST com testes unitários, execução em container Docker e pipeline de Integração Contínua utilizando GitHub Actions.

### Tecnologias utilizadas

- Python
- Flask
- Pytest
- Flake8
- Docker
- GitHub Actions
- JSON

### Estrutura do projeto

```text
trabalho04-api-jogos-multiplayer/
├── api/
│   ├── app.py
│   ├── requirements.txt
│   ├── data/
│   │   └── partidas.json
│   └── tests/
│       └── test_api.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── .gitignore
└── README.md
```

### Rotas da API

### GET /status

Retorna as informações básicas da aplicação.

Exemplo de resposta:

```json
{
  "nome": "API de Jogos Multiplayer",
  "versao": "1.0.0",
  "status": "online"
}
```

### GET /partidas

Retorna a lista de partidas multiplayer simuladas.

Exemplo de resposta:

```json
{
  "status": "sucesso",
  "quantidade": 10,
  "dados": []
}
```

### GET /partidas/{id}

Retorna uma partida específica pelo identificador.

Exemplo:

```text
GET /partidas/1
```

Caso o identificador não exista, a API retorna erro 404.

Exemplo:

```text
GET /partidas/999
```

### Como executar localmente

Clone o repositório:

```powershell
git clone https://github.com/JeanKoerich/trabalho04-api-jogos-multiplayer.git
```

Acesse a pasta do projeto:

```powershell
cd trabalho04-api-jogos-multiplayer
```

Crie o ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente virtual no PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a execução do ambiente virtual, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Depois ative novamente:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install --upgrade pip
python -m pip install -r api\requirements.txt
```

Execute a API:

```powershell
python api\app.py
```

Após executar, acesse no navegador:

```text
http://localhost:8000/status
http://localhost:8000/partidas
http://localhost:8000/partidas/1
http://localhost:8000/partidas/999
```

### Como executar os testes unitários

Entre na pasta da API:

```powershell
cd api
```

Execute os testes:

```powershell
pytest -v
```

Resultado esperado:

```text
4 passed
```

Também é possível executar os testes pela raiz do projeto:

```powershell
python -m pytest api/tests -v
```

### Análise estática com Flake8

Para executar a análise estática de código, use o comando abaixo na raiz do projeto:

```powershell
flake8 api --count --exit-zero --max-complexity=10 --max-line-length=120 --statistics
```

O resultado esperado é:

```text
0
```

### Como executar com Docker

Crie a imagem Docker:

```powershell
docker build -t api-jogos-multiplayer .
```

Execute o container:

```powershell
docker run -p 8000:8000 api-jogos-multiplayer
```

Depois acesse no navegador:

```text
http://localhost:8000/status
```

### GitHub Actions

O projeto possui um pipeline de Integração Contínua configurado com GitHub Actions.

O workflow está localizado em:

```text
.github/workflows/ci.yml
```

A cada push ou pull request na branch main, o pipeline executa as seguintes etapas:

- Checkout do código;
- Configuração do Python;
- Instalação das dependências;
- Análise estática com Flake8;
- Execução dos testes unitários com Pytest.

### Sobre os dados simulados

Os dados utilizados pela API estão no arquivo:

```text
api/data/partidas.json
```

Esse arquivo contém partidas multiplayer simuladas com informações como jogadores, pontuação, modo da partida, servidor, duração e status.

### Autor

Jean Koerich

Curso de Bacharelado em Sistemas de Informação  
Disciplina: Cloud Computing  
UNIDAVI  
2026
