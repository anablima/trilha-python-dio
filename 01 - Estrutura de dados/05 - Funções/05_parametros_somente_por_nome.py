# Parâmetros somente por posição e somente por nome
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    # A barra "/" torna (modelo, ano, placa) posicionais-only
    # O asterisco "*" torna (marca, motor, combustivel) somente por nome (keyword-only)
    print(modelo, ano, placa, marca, motor, combustivel)


# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# Inválido: não é permitido nomear parâmetros à esquerda da "/"
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
