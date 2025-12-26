linguagens = ["python", "js", "c", "java", "csharp"]
 # `sort()`: ordena in-place (padrão: ordem lexicográfica crescente)
 linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

# Lista ordenada de trás pra frente
linguagens = ["python", "js", "c", "java", "csharp"]
 linguagens.sort(reverse=True)  # ordem decrescente
print(linguagens)

# Lista ordenada por qtd de caracteres em ordem crescente
linguagens = ["python", "js", "c", "java", "csharp"]
 linguagens.sort(key=lambda x: len(x))  # chave de ordenação: tamanho
print(linguagens)

# Lista ordenada por qtd de caracteres em ordem decrescente
linguagens = ["python", "js", "c", "java", "csharp"]
 linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)
