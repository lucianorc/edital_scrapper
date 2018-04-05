# Edital Scrapper

Um simples web scrapper para uma newsletter de editais

## Objetivo

Enviar atualização sobre editais e afins por email.

## O que é preciso

- Python >= 3.6
- Pipenv
- Scrapy

## Como começar

```sh
$ pipenv shell
# Virtual Environment created
$ pipenv install
# Packages installed
$ cp .env.example .env
# .env file created
```

Depois desses comandos, basta adicionar os seus valores do domínio e da chave da API do [MailGun](http://mailgun.com) para o envio das informações por email.

## Como recuperar as informações

Basta executar no seu emulador de terminal favorito:

```sh
scrapy crawl nome_do_spider
```

Se quiser a resposta em um JSON, basta executar:

```sh
scrapy crawl nome_do_spider -o responses/nome_do_arquivo.json
```
