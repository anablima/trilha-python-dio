linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

# Juntar listas
# `extend(iterável)`: adiciona cada item de `iterável` ao final (in place)
linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]
