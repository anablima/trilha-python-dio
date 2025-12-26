linguagens = ["python", "js", "c", "java", "csharp"]

# Remove a primeira ocorrência do objeto da lista
# `remove(x)`: busca por valor; levanta `ValueError` se `x` não estiver presente
linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]
