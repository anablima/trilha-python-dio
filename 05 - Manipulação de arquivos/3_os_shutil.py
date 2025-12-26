"""
Operações de sistema de arquivos com os, shutil e pathlib:
- Criar diretório (mkdir)
- Criar arquivo (open modo "w")
- Renomear arquivo (os.rename)
- Remover arquivo (os.remove)
- Mover arquivo (shutil.move)

Atenção: verifique a existência de arquivos antes de renomear/mover/remover.
"""

import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Cria um novo diretório dentro da pasta do script
os.mkdir(ROOT_PATH / "novo-diretorio")

# Cria um novo arquivo vazio
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

# Renomeia o arquivo criado
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# Remove o arquivo renomeado
os.remove(ROOT_PATH / "alterado.txt")

# Tenta mover o arquivo original para dentro do novo diretório
# Observação: após renomear para "alterado.txt" e remover, o "novo.txt" não existe mais
# Este move pode falhar se o arquivo não existir
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
