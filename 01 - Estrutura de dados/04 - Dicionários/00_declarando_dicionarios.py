"""
Dicionários (mapeamentos chave → valor):
- Literal com chaves `{}`.
- Construtor `dict(chave=valor)`.
- Inserção/atualização via `d["chave"] = valor`.
 - As duas formas (literal e `dict`) criam o mesmo tipo.
"""

pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

# Adicionando nova chave ao dicionário
pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
