"""
Leitura e escrita de CSV com csv.writer, csv.reader e DictReader:
- writerow: escreve linha
- reader: lê linhas como listas
- DictReader: lê linhas como dicionários (usa cabeçalho)

Use newline="" e encoding="utf-8" para evitar problemas de quebra de linha e acentuação.
"""

import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1


try:
    # Cria o arquivo CSV e escreve cabeçalho + linhas
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    # Lê o CSV como listas (cada linha é uma lista)
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                # Pula o cabeçalho
                continue
            print(f"ID: {row[COLUNA_ID]}")
            print(f"Nome: {row[COLUNA_NOME]}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    # Lê o CSV como dicionários (chaves do cabeçalho)
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
