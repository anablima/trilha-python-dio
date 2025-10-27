# ---------- Comentários detalhados pelo assistente (pt-BR) ----------
# Este programa demonstra as funções mais comuns para manipulação de strings em Python
# Demonstra:
# 1. Funções de alteração de caso (upper, lower, title)
# 2. Funções de remoção de espaços (strip, rstrip, lstrip)
# 3. Funções de formatação (center, join)
# 4. Concatenação de strings

# Exemplo 1: Alteração de caso
nome = "gUIlherME"  # String com mistura de maiúsculas e minúsculas

# upper(): converte todos os caracteres para maiúsculo
print(nome.upper())  # Resultado: GUILHERME

# lower(): converte todos os caracteres para minúsculo
print(nome.lower())  # Resultado: guilherme

# title(): primeira letra de cada palavra em maiúsculo
print(nome.title())  # Resultado: Guilherme

# Exemplo 2: Remoção de espaços em branco
texto = "  Olá mundo!    "  # String com espaços extras no início e fim

# Demonstração do texto original com ponto no final
print(texto + ".")  # Mostra os espaços extras

# strip(): remove espaços em branco do início e fim
print(texto.strip() + ".")  # Remove todos os espaços extras

# rstrip(): remove espaços em branco apenas do lado direito
print(texto.rstrip() + ".")  # Remove espaços apenas do final

# lstrip(): remove espaços em branco apenas do lado esquerdo
print(texto.lstrip() + ".")  # Remove espaços apenas do início

# Exemplo 3: Formatação de texto
menu = "Python"

# Concatenação simples com string literal
print("####" + menu + "####")  # Adiciona #### antes e depois

# center(): centraliza o texto em um espaço definido
print(menu.center(14))  # Centraliza usando espaços (14 caracteres total)

# center() com caractere de preenchimento
print(menu.center(14, "#"))  # Centraliza usando # como preenchimento

# join(): une caracteres entre cada letra da string
print("-".join(menu))  # Coloca - entre cada letra: P-y-t-h-o-n
