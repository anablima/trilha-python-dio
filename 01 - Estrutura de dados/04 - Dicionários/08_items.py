contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# items(): visão dinâmica de pares (chave, valor); reflete mudanças no dicionário
resultado = contatos.items()  # dict_items([('guilherme@gmail.com', {"nome": "Guilherme", "telefone": "3333-2221"})])
print(resultado)
