"""
Demonstração de `input()` e `print()`:
- `input(msg)`: lê texto do usuário mostrando a mensagem `msg`.
- `print(*args, sep, end)`: exibe valores; `sep` define separador e `end` o final da linha.
"""

# Captura de dados via input (sempre retorna string)
nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

# Impressão padrão: separador por espaço, finaliza com "\n"
print(nome, idade)

# Personalizando o final da linha com `end`
print(nome, idade, end="...\n")

# Personalizando separador com `sep` e o final com `end`
print(nome, idade, sep="#", end="...\n")

# Apenas separador customizado, final padrão ("\n")
print(nome, idade, sep="#")
