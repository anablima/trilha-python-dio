contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# popitem(): remove e retorna o último par inserido (ordem de inserção)
resultado = contatos.popitem()  # ('guilherme@gmail.com', {"nome": "Guilherme", "telefone": "3333-2221"})
print(resultado)

# contatos.popitem()  # KeyError
 # em dicionário vazio, levanta KeyError
