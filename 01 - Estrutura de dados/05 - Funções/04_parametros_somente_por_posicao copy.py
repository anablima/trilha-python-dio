def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    # A barra "/" define parâmetros somente por posição à esquerda
    # (modelo, ano, placa devem ser passados como posicionais)
    print(modelo, ano, placa, marca, motor, combustivel)


# Válido: parâmetros à esquerda da "/" passados por posição
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# Inválido: usar nomes para parâmetros posicionais-only → TypeError
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
