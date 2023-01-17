Esse projeto foi um teste para o processo seletivo da empresa Seazone, o desafio era criar 3 APIs Restful utilizando o Framework Django com a linguagem Python. As APIs são relacionadas a aluguel de imoveis.

<details>
<summary><strong>Como rodar</strong></summary><br />

**Ambiente de desenvolvimento:**
  - Rode o comando `python3 -m venv env` para criar seu ambiente de desenvolvimento.
  - Rode o comando `env/Scripts/activate.bat` para acessar seu ambiente de desenvolvimento.

**Dependencias:**
  - Rode o comando `pip install django`
  - Rode o comando `pip install django_rest_framework`
  - Rode o comando `pip install requests`
  
**Start up:**
 - Rode o comando `python3 manage.py makemigrations`
 - Rode o comando `python3 manage.py migrate`
 - Rode o comando `python3 manage.py seed`
 - Por fim rode o comando `python3 manage.py runserver` para startar a aplicação.

**Testes:**
 - Rode o comando `python3 manage.py test` para rodas os testes da aplicação.

</details>

<details>
<summary><strong>Imovel API</strong></summary><br />

**`GET /imovel`**
 - Retorna todos imoveis:
```json
[
    {
        "id": "<imovelId>",
        "max_hospedes": "<max_hospedes>",
        "banheiros": "<banheiros>",
        "pet": "<pet>",
        "limpeza": "<limpeza>",
        "ativacao": "<ativacao>",
        "criacao": "<criacao>",
        "atualizacao": "<atualizacao>",
        "anuncios": ["<anuncios.id: anuncios.plataforma>"],
    },
    {
        "imovel 2 ..."
    }
]
```

**`GET /imovel/<imovel_id>`**
 - Retorna o imovel do id mencionado:
```json
{
    "id": "<imovelId>",
    "max_hospedes": "<max_hospedes>",
    "banheiros": "<banheiros>",
    "pet": "<pet>",
    "limpeza": "<limpeza>",
    "ativacao": "<ativacao>",
    "criacao": "<criacao>",
    "atualizacao": "<atualizacao>",
    "anuncios": ["<anuncios.id: anuncios.plataforma>"],
}
```

**`POST /imovel`**
 - Você deve preencher o body com os campos `max_hospedes`, `banheiros`, `pet` e `limpeza` exemplo:
 ```json
{
    "max_hospedes": 3,
    "banheiros": 2,
    "pet": true,
    "limpeza": 150.50
}
```
 - Em caso de sucesso, retorna as informações do imovel criado:
```json
{
    "id": "<imovelId>",
    "max_hospedes": "<max_hospedes>",
    "banheiros": "<banheiros>",
    "pet": "<pet>",
    "limpeza": "<limpeza>",
    "ativacao": "<ativacao>",
    "criacao": "<criacao>",
    "atualizacao": "<atualizacao>",
    "anuncios": ["<anuncios.id: anuncios.plataforma>"],
}
```

**`PUT /imovel/<imovel_id>`**
 - Você deve preencher o body com os campos `max_hospedes`, `banheiros`, `pet` e `limpeza` exemplo:
 ```json
{
    "max_hospedes": 4,
    "banheiros": 2,
    "pet": true,
    "limpeza": 150.50
}
```
 - Em caso de sucesso, retorna as informações do imovel atualizado:
```json
{
    "id": "<imovelId>",
    "max_hospedes": "<max_hospedes>",
    "banheiros": "<banheiros>",
    "pet": "<pet>",
    "limpeza": "<limpeza>",
    "ativacao": "<ativacao>",
    "criacao": "<criacao>",
    "atualizacao": "<atualizacao>",
    "anuncios": ["<anuncios.id: anuncios.plataforma>"],
}
```

**`DEL /imovel/<imovel_id>`**
 - Em caso de sucesso, retorna as informações de sucesso:
```json
{
    "res": "Object deleted!"
}
```
</details>

<details>
<summary><strong>Anuncio API</strong></summary><br />

**`GET /anuncio`**
 - Retorna todos anuncios:
```json
[
    {
        "id": "<anuncio_id>",
        "imovel_id": "<imovel_id>",
        "plataforma": "<plataforma>",
        "taxa_plataforma": "<taxa_plataforma>",
        "criacao": "<criacao>",
        "atualizacao": "<atualizacao>",
        "reservas": ["<reservas.id: reservas.preco_total>"],
    },
    {
        "anuncio 2 ..."
    }
]
```

**`GET /anuncio/<anuncio_id>`**
 - Retorna o anuncio do id mencionado:
```json
{
    "id": "<anuncio_id>",
    "imovel_id": "<imovel_id>",
    "plataforma": "<plataforma>",
    "taxa_plataforma": "<taxa_plataforma>",
    "criacao": "<criacao>",
    "atualizacao": "<atualizacao>",
    "reservas": ["<reservas.id: reservas.preco_total>"],
}
```

**`POST /anuncio`**
 - Você deve preencher o body com os campos `imovel_id`, `plataforma` e `taxa_plataforma` exemplo:
 ```json
{
    "imovel_id": "valid imovel id",
    "plataforma": "AirBnB",
    "taxa_plataforma": 150.50
}
```
 - Em caso de sucesso, retorna as informações do anuncio criado:
```json
{
    "id": "<anuncio_id>",
    "imovel_id": "<imovel_id>",
    "plataforma": "<plataforma>",
    "taxa_plataforma": "<taxa_plataforma>",
    "criacao": "<criacao>",
    "atualizacao": "<atualizacao>",
    "reservas": ["<reservas.id: reservas.preco_total>"],
}
```

**`PUT /anuncio/<anuncio_id>`**
 - Você deve preencher o body com os campos `imovel_id`, `plataforma` e `taxa_plataforma` exemplo:
 ```json
{
    "imovel_id": "valid imovel id",
    "plataforma": "AirBnB",
    "taxa_plataforma": 150.50
}
```
 - Em caso de sucesso, retorna as informações do anuncio atualizado:
```json
{
    "id": "<anuncio_id>",
    "imovel_id": "<imovel_id>",
    "plataforma": "<plataforma>",
    "taxa_plataforma": "<taxa_plataforma>",
    "criacao": "<criacao>",
    "atualizacao": "<atualizacao>",
    "reservas": ["<reservas.id: reservas.preco_total>"],
}
```

</details>

<details>
<summary><strong>Reserva API</strong></summary><br />

**`GET /reserva`**
 - Retorna todas reservas:
```json
[
    {
        "id": "<reserva_id>",
        "anuncio_id": "<anuncio_id>",
        "check_in": "<check_in>",
        "check_out": "<check_out>",
        "preco_total": "<preco_total>",
        "comentario": "<comentario>",
        "hospedes": "<hospedes>",
        "criacao": "<criacao>",
        "atualizacao": "<atualizacao>",
    },
    {
        "reserva 2 ..."
    }
]
```

**`GET /reserva/<reserva_id>`**
 - Retorna reserva do id mencionado:
```json
{
    "id": "<reserva_id>",
    "anuncio_id": "<anuncio_id>",
    "check_in": "<check_in>",
    "check_out": "<check_out>",
    "preco_total": "<preco_total>",
    "comentario": "<comentario>",
    "hospedes": "<hospedes>",
    "criacao": "<criacao>",
    "atualizacao": "<atualizacao>",
}
```

**`POST /reserva`**
 - Você deve preencher o body com os campos `anuncio_id`, `check_in`, `check_out`, `preco_total`, `comentario` `hospedes` exemplo:
 ```json
{
    "anuncio_id": "10145e55-6bc1-4e1c-b6f4-22dee9369f67",
    "check_in": "2020-05-21",
    "check_out": "2020-04-23",
    "preco_total": 500.50,
    "comentario": "gostei muito",
    "hospedes": 3
}
```
 - Em caso de sucesso, retorna as informações da reserva criada:
```json
{
    "id": "<reserva_id>",
    "anuncio_id": "<anuncio_id>",
    "check_in": "<check_in>",
    "check_out": "<check_out>",
    "preco_total": "<preco_total>",
    "comentario": "<comentario>",
    "hospedes": "<hospedes>",
    "criacao": "<criacao>",
    "atualizacao": "<atualizacao>",
}
```

**`DEL /reserva/<reserva_id>`**
 - Em caso de sucesso, retorna as informações de sucesso:
```json
{
    "res": "Object deleted!"
}
```

</details>
