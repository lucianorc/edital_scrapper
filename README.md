# Edital Scrapper

Um simples web scrapper para uma newsletter de editais

## Objetivo

Enviar atualização sobre editais e afins por email para as pessoas interessadas

## O que é preciso

- Python >= 3.6
- Pipenv
- Scrapy

## Como recuperar as informações

Basta executar no seu emulador de terminal favorito:

```sh
scrapy crawl nome_do_spider
```

Se quiser a resposta em um JSON, basta executar:

```sh
scrapy crawl nome_do_spider -o responses/nome_do_arquivo.json
```
