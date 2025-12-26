"""
Boas práticas na manipulação de arquivos:
- Usar with open para fechar automaticamente
- Tratar exceções específicas (IOError, UnicodeDecodeError)
- Definir encoding ao lidar com textos (ex.: UTF-8)
"""

from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    # Lê um arquivo (exemplo) usando with: fecha automaticamente
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")


# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")

try:
    # Lê arquivo explicitando encoding UTF-8; evita erros de decodificação
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
except UnicodeDecodeError as exc:
    print(exc)
