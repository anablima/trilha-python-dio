# ---------- Comentários detalhados pelo assistente (pt-BR) ----------
# Este programa demonstra diferentes formas de usar o loop for em Python
# O loop for é usado para iteração determinada (número conhecido de repetições)
# Demonstra:
# 1. Iteração sobre strings
# 2. Uso da função range()
# 3. Diferentes formas de usar range()
# 4. Cláusula else em loops
# 5. Parâmetro end do print()

# Entrada de dados para exemplo de iteração sobre string
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"  # Constante com as vogais para comparação

# Exemplo 1: Iterando sobre uma string (texto é iterável)
# Procura e imprime apenas as vogais do texto
for letra in texto:
    if letra.upper() in VOGAIS:  # Converte para maiúsculo para comparar
        print(letra, end="")     # end="" evita quebra de linha
else:
    # O bloco else é executado quando o loop termina normalmente
    # (não é interrompido por break)
    print()  # Adiciona uma quebra de linha no final

# Exemplo 2: range() com um argumento
# range(stop) gera números de 0 até stop-1
print("\nContagem de 0 a 5:")
for numero in range(6):  # Gera: 0, 1, 2, 3, 4, 5
    print(numero, end=" ")
print()  # Quebra de linha

# Exemplo 3: range() com dois argumentos
# range(start, stop) gera números de start até stop-1
print("\nContagem de 1 a 5:")
for numero in range(1, 6):  # Gera: 1, 2, 3, 4, 5
    print(numero, end=" ")
print()  # Quebra de linha

# Exemplo 4: range() com três argumentos
# range(start, stop, step) gera números de start até stop-1, pulando de step em step
print("\nTabuada do 5 (0 a 50):")
for numero in range(0, 51, 5):  # Gera: 0, 5, 10, 15, ..., 45, 50
    print(numero, end=" ")
print()  # Quebra de linha final
