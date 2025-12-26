def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# Chamada com argumentos posicionais (ordem importa)
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
# Chamada com argumentos nomeados (ordem não importa; nomes devem bater)
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
# Desempacotando um dicionário em argumentos nomeados com **
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
