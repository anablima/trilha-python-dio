contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# pop(chave[, padrao]): remove a chave e retorna o valor
# sem padrão e chave ausente → levanta KeyError
resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# com padrão, evita erro quando a chave não existe
resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
