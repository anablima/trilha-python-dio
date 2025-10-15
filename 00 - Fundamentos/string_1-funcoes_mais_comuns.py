nome = "gUIlherME"

# Tudo maiúscula
print(nome.upper())

# Tudo minúsculo
print(nome.lower())

# Primeira letra em maiúsculo
print(nome.title())

texto = "  Olá mundo!    "

print(texto + ".")

# Eliminando todos os espaços em branco
print(texto.strip() + ".")

# Eliminando espaços em branco do lado direito da string
print(texto.rstrip() + ".")

# Eliminando espaços em branco do lado esquerdo da string
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#")) # Centraliza a string
print("-".join(menu)) # Junta o caractere na string
