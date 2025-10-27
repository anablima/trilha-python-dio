# ---------- Comentários detalhados pelo assistente (pt-BR) ----------
# Este programa demonstra diferentes formas de ler arquivos em Python
# Demonstra:
# 1. Leitura completa do arquivo (read)
# 2. Leitura linha a linha (readline)
# 3. Leitura de todas as linhas em lista (readlines)
# 4. Leitura iterativa com while
# 5. Abertura e fechamento correto de arquivos

# IMPORTANTE: Ajuste o caminho do arquivo para seu ambiente
CAMINHO_ARQUIVO = "/Users/anabeatrizferreiralima/Documents/BootcampPython-DIO/trilha-python-dio/05 - Manipulação de arquivos/lorem.txt"

# Exemplo 1: Leitura completa do arquivo
# open(): abre o arquivo no modo leitura ('r')
arquivo = open(CAMINHO_ARQUIVO, "r")
# read(): lê todo o conteúdo do arquivo em uma única string
print(arquivo.read())
arquivo.close()  # Sempre feche o arquivo após usar

# Exemplo 2: Leitura de uma única linha
arquivo = open(CAMINHO_ARQUIVO, "r")
# readline(): lê apenas a próxima linha do arquivo
print(arquivo.readline())
arquivo.close()

# Exemplo 3: Leitura de todas as linhas em lista
arquivo = open(CAMINHO_ARQUIVO, "r")
# readlines(): lê todas as linhas e retorna uma lista
# Cada elemento da lista é uma linha do arquivo
print(arquivo.readlines())
arquivo.close()

# Exemplo 4: Leitura iterativa linha por linha
arquivo = open(CAMINHO_ARQUIVO, "r")
# Usa operador de atribuição em expressão (:=) - Python 3.8+
# len(linha := arquivo.readline()): atribui próxima linha à variável e verifica se não está vazia
while len(linha := arquivo.readline()):
    print(linha)  # Imprime cada linha
arquivo.close()

# Observação: Em código de produção, prefira usar 'with':
# with open(CAMINHO_ARQUIVO, 'r') as arquivo:
#     # código aqui
# O 'with' garante que o arquivo será fechado automaticamente
