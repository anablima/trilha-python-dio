contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# setdefault(chave, padrao): se a chave existir, retorna o valor atual
contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

# se não existir, insere a chave com o valor padrão e o retorna
contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
