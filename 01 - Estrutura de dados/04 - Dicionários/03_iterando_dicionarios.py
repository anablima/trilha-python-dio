contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Iterando sobre o dicionário: por padrão, percorre as chaves
for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

# items(): retorna pares (chave, valor) para iterar diretamente
for chave, valor in contatos.items():
    print(chave, valor)
