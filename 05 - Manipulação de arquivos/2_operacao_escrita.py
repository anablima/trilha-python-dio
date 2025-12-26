"""
Demonstra escrita em arquivos com open() e modos:
- Modo "w": cria/substitui arquivo e permite escrita
- write(): escreve string
- writelines(): escreve lista de strings linha a linha

Observação: ajuste o caminho para seu ambiente (macOS) e prefira Path.
"""

# Abre o arquivo no modo escrita ("w"): cria ou sobrescreve se existir
arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/teste.txt", "w"
)
# Escreve uma única linha de texto
arquivo.write("Escrevendo dados em um novo arquivo.")
# Escreve múltiplas linhas a partir de uma lista de strings
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
# Sempre feche o arquivo após terminar a escrita
arquivo.close()
arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/teste.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()
