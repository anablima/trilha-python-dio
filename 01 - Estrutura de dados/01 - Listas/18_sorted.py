linguagens = ["python", "js", "c", "java", "csharp"]

# `sorted(iterável, ...)`: retorna nova lista ordenada (não altera original)
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]
