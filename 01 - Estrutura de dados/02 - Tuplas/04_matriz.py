matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])     # 1 (linha 0, coluna 0)
print(matriz[0][-1])    # 2 (última coluna da linha 0)
print(matriz[-1][-1])   # "c" (última linha, última coluna)
