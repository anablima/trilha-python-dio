# Loop for deve ser usando quando sabemos a qtd de vezes que nosso loop será executado

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha

# Exemplos utilizando a função built-in 

# range(stop) -> range object
for numero in range(6):
    print(numero,'\n')

# range(start, stop) -> range object
for numero in range(1, 6):
    print(numero,'\n')

# Tabuada do 5, usando range(start, stop[,step]) -> range object
for numero in range(0, 51, 5):
    print(numero, end=" ")
