"""
Tratamento de erros ao abrir arquivos:
- FileNotFoundError: arquivo não existe
- IsADirectoryError: caminho aponta para diretório, não arquivo
- IOError: erros gerais de I/O
- Exception: captura qualquer outro erro não previsto
"""

from pathlib import Path

ROOT_PATH = Path(__file__).parent


try:
    # Tenta abrir arquivo em subdiretório
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    print(exc)
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")


# try:
#     arquivo = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")
