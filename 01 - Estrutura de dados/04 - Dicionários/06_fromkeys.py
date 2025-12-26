resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
# fromkeys(iterável, valor_padrao=None): cria chaves a partir do iterável
# todas as chaves recebem o mesmo valor padrão
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
# se usar um objeto mutável como valor, todas as chaves apontarão para o mesmo objeto
print(resultado)
