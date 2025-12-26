"""
Indexação e fatiamento de strings:
- Strings são sequências imutáveis; suportam índices e slices.
- `s[a:b:c]` → início `a`, fim `b` (exclusivo), passo `c`.
"""

nome = "Guilherme Arthur de Carvalho"

print(nome[0])        # primeiro caractere
print(nome[-2])       # penúltimo caractere
print(nome[:9])       # do início até índice 8
print(nome[10:])      # do índice 10 até o fim
print(nome[10:16])    # do índice 10 ao 15
print(nome[10:16:2])  # com passo 2 (pula caracteres)
print(nome[:])        # cópia inteira
print(nome[::-1])     # reverso (passo negativo)
