nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

# Interpolação estilo C (antiga): usa especificadores de formato (%s, %d)
# Interpolação estilo C (deprecated para muitos casos)
print("Nome: %s Idade: %d" % (nome, idade))

# Método format com chaves como placeholders
# Método format com placeholders posicionais
print("Nome: {} Idade: {}".format(nome, idade))

# Placeholders com índices (reuso de argumentos)
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

# Placeholders nomeados: passam clareza ao indicar por nome
# Placeholders nomeados
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
# Desempacotando dicionário com ** para preencher nomes
print("Nome: {nome} Idade: {idade}".format(**dados))

# f-strings (Python 3.6+): expressões inline mais legíveis
print(f"Nome: {nome} Idade: {idade}")
# Formatação numérica: 2 casas decimais
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
# Largura mínima 10 e 1 casa decimal
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
