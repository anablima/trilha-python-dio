# ---------- Comentários detalhados pelo assistente (pt-BR) ----------
# Este programa demonstra diferentes formas de usar estruturas condicionais em Python
# Demonstra:
# 1. if simples
# 2. if/else
# 3. if/elif/else
# 4. Uso de constantes
# 5. Entrada de dados do usuário

# Definição de constantes (em maiúsculas por convenção)
MAIOR_IDADE = 18      # Idade mínima para CNH
IDADE_ESPECIAL = 17   # Idade para casos especiais

# Entrada de dados: converte string para inteiro
idade = int(input("Informe sua idade: "))

# Exemplo 1: if simples (sem else)
# Verifica apenas uma condição
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

# Exemplo 2: if simples complementar
# Verifica a condição oposta em outro if
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


# Exemplo 3: if com else
# Trata os dois casos possíveis (verdadeiro/falso)
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CNH.")


# Exemplo 4: if com elif e else
# Trata múltiplos casos específicos e um caso padrão
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL:  # Condição adicional verificada se o if for falso
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:  # Executado se nenhuma condição anterior for verdadeira
    print("Ainda não pode tirar a CNH.")
