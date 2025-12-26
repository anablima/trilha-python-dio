# Demonstração simples de boas práticas:
# - Imports da biblioteca padrão
# - Impressão/inspeção rápida de módulos
# - Variáveis e listas (coleções) com nomes claros
# Observação: este arquivo é didático; não segue um caso real.
import os
import sys

# Imprime a representação dos módulos carregados.
# Útil apenas para inspeção/debug rápido; normalmente não se imprime módulos em produção.
print(os)
print(sys)

# Variável de texto (string) com um nome simples.
# Em código real, evite nomes de uma letra (ex.: "a"); prefira nomes descritivos.
a = "python"

# Exemplo de string longa.
# Boas práticas (PEP 8) sugerem manter linhas até ~79/88 caracteres.
# Para strings longas, prefira quebrar em múltiplas linhas com concatenação implícita (
# "parte1"
# "parte2"), ou usar parênteses.
b = "ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"

# Lista de frutas: coleção ordenada e mutável de strings.
# Você pode iterar, adicionar/remover itens e acessar por índice.
frutas = [
    "pera",
    "maçã",
    "laranja",
    "uva",
    "melão",
    "morango",
    "abacate",
    "banana",
    "carambola",
    "pessego",
    "tamara",
    "melancia",
]

# Lista de carros: outro exemplo de coleção simples.
# Dica: manter consistência de estilo (aspas simples ou duplas) em todo o projeto.
carros = ["ferrari", "brasilia", "gol", "up"]
