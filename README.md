# Pokémon API - Projeto Final Backend

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Pytest](https://img.shields.io/badge/Tests-Pytest-yellow)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-black)

API RESTful desenvolvida com Python e FastAPI, integrada à PokeAPI, com paginação, autenticação via API Key, cache com Redis, testes automatizados, Docker, CI/CD e deploy no Render.

## Objetivo do Projeto

Construir uma API RESTful utilizando Python que consome dados da API pública da Pokémon e disponibiliza os dados de forma paginada.

O projeto contempla:

* Consumo da PokeAPI
* Estruturação em camadas
* Paginação
* Busca de Pokémon por nome
* Cache com Redis
* Dockerização
* Testes automatizados
* Cobertura de testes
* Lint com Ruff
* CI/CD com GitHub Actions
* Deploy automatizado no Render
* Variáveis de ambiente
* Proteção por API Key
* Middleware de logging
* Tratamento global de exceções

---
## Deploy

https://pokemon-api-u9so.onrender.com

## API Access

Esta API utiliza autenticação via API Key.

Utilize o seguinte header para acessar os endpoints protegidos:

```bash
x-api-key: pokemon123
```

## Endpoints disponíveis

- `/` → Status da API
- `/docs` → Documentação Swagger
- `/pokemons/` → Lista de Pokémon

---

# Stack e Tecnologias

* Python 3.12
* FastAPI
* Pydantic
* SQLAlchemy
* Pytest
* Pytest-Cov
* HTTPX
* Ruff
* Docker
* Docker Compose
* Redis
* GitHub Actions
* Render

---

# 📂 Estrutura do Projeto

```bash
pokemon-api/
│
├── app/
│   ├── core/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── tests/
│   ├── test_router.py
│   └── test_services.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Arquitetura do Projeto

O projeto foi organizado seguindo separação de responsabilidades:

- `core/` → configurações, segurança, logs e banco de dados
- `models/` → modelos da aplicação
- `routes/` → definição dos endpoints
- `schemas/` → validação e serialização dos dados
- `services/` → regras de negócio e integração com a PokeAPI
- `utils/` → funcionalidades auxiliares
- `tests/` → testes automatizados

---

# Funcionalidades

* Paginação
* Busca por nome
* Cache com Redis
* Logging de requisições via middleware
* Tratamento global de exceções
* Autenticação via API Key

## Listagem de Pokémons

Endpoint responsável por retornar os Pokémons de forma paginada.

### Endpoint

```http
GET /pokemons/
```

### Query Params

| Parâmetro | Tipo | Descrição                      |
| --------- | ---- | ------------------------------ |
| limit     | int  | Quantidade de itens por página |
| offset    | int  | Deslocamento da paginação      |

### Exemplo

```http
GET /pokemons/?limit=10&offset=0
```

### Exemplo de Resposta

```json
{
  "count": 1302,
  "next": "https://pokeapi.co/api/v2/pokemon?offset=10&limit=10",
  "previous": null,
  "results": [
    {
      "name": "bulbasaur",
      "url": "https://pokeapi.co/api/v2/pokemon/1/"
    }
  ]
}
```

## Busca de Pokémon por Nome

### Endpoint

```http
GET /pokemons/{name}
```

### Exemplo

```http
GET /pokemons/pikachu
```

---

# Autenticação com API Key

A API utiliza autenticação simples via API Key.

É necessário enviar o header:

```http
x-api-key: SUA_API_KEY
```

Caso a chave seja inválida:

```json
{
  "detail": "Invalid API Key"
}
```

---

# Docker

## Build da aplicação

```bash
docker compose build
```

## Subir containers

```bash
docker compose up
```

## Derrubar containers

```bash
docker compose down
```

---

# Executando Localmente

## 1. Clonar o repositório

```bash
git clone https://github.com/IsabelleLandini/pokemon-api.git
```

---

## 2. Acessar a pasta do projeto

```bash
cd pokemon-api
```

---

## 3. Instalar Poetry

```bash
pip install poetry
```

---

## 4. Instalar dependências

```bash
poetry install
```

---

## 5. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=sqlite:///./pokemon.db
POKEAPI_URL=https://pokeapi.co/api/v2
REDIS_URL=redis://redis:6379
API_KEY=pokemon123
```

---

## 6. Executar a aplicação

```bash
poetry run uvicorn app.main:app --reload
```

A aplicação estará disponível em:

```bash
http://127.0.0.1:8000
```

---

# Testes Automatizados

O projeto possui testes automatizados utilizando Pytest.

## Executar testes

```bash
poetry run pytest
```

## Executar testes com cobertura

```bash
poetry run pytest --cov=app
```
O pipeline exige cobertura mínima de 80%.

---

# Documentação Swagger

## Ambiente local

```bash
http://127.0.0.1:8000/docs
```

## Ambiente de produção

```bash
https://pokemon-api-u9so.onrender.com/docs
```

---

# CI/CD

O projeto utiliza GitHub Actions para integração contínua.

## Pipeline executa:

* Instalação das dependências
* Verificação de lint com Ruff
* Execução dos testes automatizados
* Validação de cobertura de testes
* Build da aplicação Docker
* Validação do container
* Deploy automático

O deploy é realizado automaticamente no Render após push na branch principal.

---

# Deploy

Aplicação disponível em produção no Render:

```bash
https://pokemon-api-u9so.onrender.com
```

## Exemplo de endpoint

```bash
https://pokemon-api-u9so.onrender.com/pokemons/
```
A API requer autenticação via `x-api-key`.

---

# 👩‍💻 Desenvolvedora

Isabelle Landini

Projeto desenvolvido como projeto final de Backend utilizando Python.
