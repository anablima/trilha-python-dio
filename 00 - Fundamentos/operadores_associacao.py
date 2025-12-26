"""
Operadores de associação:
- `in`: verifica se um elemento pertence a uma sequência/coleção.
- `not in`: verifica a não-pertinência.
"""

frutas = ["limao", "uva"]
curso = "Curso de python"

print("laranja" not in frutas)  # True: "laranja" não está na lista
print("limao" in frutas)        # True: "limao" está na lista
print("Python" in curso)        # False: case-sensitive, "Python" ≠ "python"
