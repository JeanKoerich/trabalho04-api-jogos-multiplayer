# API de Jogos Multiplayer

## Descrição

Este projeto foi desenvolvido para o Trabalho Final da disciplina de **Cloud Computing**, do curso de Sistemas de Informação da UNIDAVI.

A aplicação consiste em uma **API REST** relacionada ao tema de **servidor de jogos multiplayer**, mantendo continuidade com os trabalhos anteriores da disciplina. A API disponibiliza dados simulados de partidas multiplayer, permitindo consultar o status da aplicação, listar partidas cadastradas em um arquivo JSON externo e buscar uma partida específica pelo identificador.

O projeto também conta com **testes unitários** e um pipeline de **Integração Contínua (CI)** utilizando **GitHub Actions**, garantindo que os testes sejam executados automaticamente a cada alteração enviada ao repositório.

## Objetivo do projeto

O objetivo principal é demonstrar a construção de uma API REST simples, documentada e testável, aplicando conceitos de Cloud Computing e DevOps.

A API foi criada para simular parte do funcionamento de um sistema de jogos multiplayer, onde partidas podem ser consultadas por meio de rotas HTTP. Os dados utilizados são simulados, porém estruturados de forma coerente com o domínio do projeto.

## Tecnologias utilizadas

* Python 3.11
* Flask
* Pytest
* Flake8
* Docker
* GitHub Actions
* JSON

## Estrutura do projeto

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

## Explicação dos principais arquivos

### `api/app.py`

Arquivo principal da aplicação. Ele contém a configuração da API Flask e as rotas disponíveis no projeto.

Responsabilidades:

* iniciar a aplicação Flask;
* carregar os dados do arquivo `partidas.json`;
* disponibilizar a rota `GET /status`;
* disponibilizar a rota `GET /partidas`;
* disponibilizar a rota `GET /partidas/{id}`;
* retornar respostas em formato JSON;
* tratar erros como recurso não encontrado e falha interna.

### `api/data/partidas.json`

Arquivo externo responsável por armazenar os dados simulados das partidas multiplayer.

Esse arquivo foi separado do código principal para manter melhor organização e para simular uma fonte externa de dados.

### `api/tests/test_api.py`

Arquivo contendo os testes unitários da API.

Os testes verificam se as principais rotas estão funcionando corretamente, se os retornos HTTP estão adequados e se a estrutura JSON esperada está sendo entregue.

### `api/requirements.txt`

Arquivo que lista as dependências necessárias para executar o projeto.

Ele é utilizado tanto na execução local quanto no pipeline do GitHub Actions e no build da imagem Docker.

### `.github/workflows/ci.yml`

Arquivo responsável pela configuração do pipeline de Integração Contínua com GitHub Actions.

O pipeline executa automaticamente:

* checkout do código;
* configuração do Python;
* instalação das dependências;
* análise estática com Flake8;
* execução dos testes unitários com Pytest.

### `Dockerfile`

Arquivo utilizado para criar uma imagem Docker da API, permitindo executar a aplicação em container.

## Rotas da API

### GET `/status`

Retorna informações de saúde da aplicação.

Exemplo de resposta:

```json
{
  "nome": "API de Jogos Multiplayer",
  "versao": "1.0.0",
  "status": "online"
}
```

Código HTTP esperado:

```text
200 OK
```

---

### GET `/partidas`

Retorna a lista de partidas multiplayer simuladas.

Exemplo de resposta:

```json
{
  "dados": [
    {
      "id": 1,
      "jogador1": "Rennascido",
      "jogador2": "Teste01",
      "pontos_jogador1": 17,
      "pontos_jogador2": 14,
      "status": "finalizada",
      "modo": "ranked",
      "servidor": "sa-east-1",
      "duracao_minutos": 8
    }
  ],
  "quantidade": 10,
  "status": "sucesso"
}
```

Código HTTP esperado:

```text
200 OK
```

---

### GET `/partidas/{id}`

Retorna uma partida específica pelo identificador.

Exemplo:

```text
GET /partidas/1
```

Exemplo de resposta:

```json
{
  "dados": {
    "id": 1,
    "jogador1": "Rennascido",
    "jogador2": "Teste01",
    "pontos_jogador1": 17,
    "pontos_jogador2": 14,
    "status": "finalizada",
    "modo": "ranked",
    "servidor": "sa-east-1",
    "duracao_minutos": 8
  },
  "status": "sucesso"
}
```

Código HTTP esperado:

```text
200 OK
```

Caso o identificador não exista:

```text
GET /partidas/999
```

Exemplo de resposta:

```json
{
  "mensagem": "Partida não encontrada",
  "status": "erro"
}
```

Código HTTP esperado:

```text
404 Not Found
```

## Como executar o projeto localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/JeanKoerich/trabalho04-api-jogos-multiplayer.git
```

Acessar a pasta:

```bash
cd trabalho04-api-jogos-multiplayer
```

### 2. Criar ambiente virtual

No Windows:

```bash
python -m venv .venv
```

### 3. Ativar ambiente virtual

No PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a execução do script, execute:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Depois tente ativar novamente:

```bash
.venv\Scripts\Activate.ps1
```

### 4. Instalar dependências

```bash
python -m pip install --upgrade pip
python -m pip install -r api\requirements.txt
```

### 5. Executar a API

```bash
python api\app.py
```

A aplicação ficará disponível em:

```text
http://localhost:8000
```

## Exemplos de acesso

Status da API:

```text
http://localhost:8000/status
```

Lista de partidas:

```text
http://localhost:8000/partidas
```

Buscar partida pelo ID:

```text
http://localhost:8000/partidas/1
```

Buscar partida inexistente:

```text
http://localhost:8000/partidas/999
```

## Como executar os testes unitários

Com o ambiente virtual ativado, acesse a pasta `api`:

```bash
cd api
```

Execute os testes:

```bash
pytest -v
```

Resultado esperado:

```text
4 passed
```

## Testes implementados

Foram implementados quatro testes unitários:

1. Verifica se a rota `GET /partidas` retorna HTTP 200.
2. Valida se o JSON retornado por `/partidas` possui os campos obrigatórios.
3. Verifica se a rota `GET /partidas/999` retorna HTTP 404.
4. Verifica se a rota `GET /status` retorna a API como online.

## Como executar a análise estática

Na raiz do projeto, execute:

```bash
flake8 api --count --exit-zero --max-complexity=10 --max-line-length=120 --statistics
```

O Flake8 foi utilizado como etapa adicional no pipeline de CI, ajudando a identificar problemas de padrão e qualidade no código.

## Como executar com Docker

### 1. Gerar a imagem Docker

Na raiz do projeto:

```bash
docker build -t api-jogos-multiplayer .
```

### 2. Executar o container

```bash
docker run -p 8000:8000 api-jogos-multiplayer
```

### 3. Acessar a API

```text
http://localhost:8000/status
```

## Integração Contínua com GitHub Actions

O projeto utiliza GitHub Actions para executar automaticamente o pipeline de Integração Contínua.

O workflow está localizado em:

```text
.github/workflows/ci.yml
```

O pipeline é executado a cada `push` ou `pull request` na branch `main`.

Etapas executadas no pipeline:

1. Checkout do código-fonte;
2. Configuração do Python 3.11;
3. Instalação das dependências;
4. Análise estática com Flake8;
5. Execução dos testes unitários com Pytest.

Essa configuração garante que alterações enviadas ao repositório sejam validadas automaticamente antes de serem consideradas estáveis.

## Relação com Cloud Computing e DevOps

O projeto aplica conceitos importantes de Cloud Computing e DevOps, como:

* construção de API REST;
* separação entre código e dados simulados;
* versionamento com Git e GitHub;
* testes unitários automatizados;
* execução em container Docker;
* pipeline de Integração Contínua com GitHub Actions.

A proposta simula um fluxo básico utilizado em ambientes reais de desenvolvimento, onde o código é versionado, testado automaticamente e preparado para execução em ambiente conteinerizado.

## Possíveis melhorias futuras

Algumas melhorias que poderiam ser aplicadas em uma versão futura:

* adicionar banco de dados real;
* implementar rotas POST, PUT e DELETE;
* adicionar autenticação;
* gerar documentação Swagger/OpenAPI;
* publicar a API em ambiente de nuvem;
* criar pipeline de deploy contínuo;
* adicionar relatório de cobertura de testes.

## Autor

Jean Koerich

Curso: Sistemas de Informação
Disciplina: Cloud Computing
Professor: Prof. Esp. Ademar Perfoll Junior
Instituição: UNIDAVI
