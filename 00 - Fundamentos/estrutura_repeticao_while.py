# ---------- Comentários detalhados pelo assistente (pt-BR) ----------
# Este programa demonstra o uso do loop while em Python
# O while é usado para iteração indeterminada (não sabemos quantas repetições)
# Demonstra:
# 1. Loop while com condição de saída
# 2. Estrutura de menu interativo
# 3. Uso de else com while
# 4. Entrada de dados do usuário
# 5. Estruturas condicionais dentro do loop

# Inicialização da variável de controle
# Usamos -1 para garantir que o loop execute pelo menos uma vez
opcao = -1

# Loop while: executa enquanto a condição for verdadeira
# Neste caso, continua executando até o usuário escolher 0 (Sair)
while opcao != 0:
    # Menu de opções usando input()
    # \n representa quebra de linha para melhor formatação
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    # Estrutura condicional para tratar as escolhas do usuário
    if opcao == 1:
        print("Sacando...")  # Simulação de operação de saque
    elif opcao == 2:
        print("Exibindo o extrato...")  # Simulação de exibição de extrato
else:
    # O bloco else é executado quando a condição do while se torna falsa
    # Neste caso, quando o usuário escolhe sair (opcao == 0)
    print("Obrigado por usar nosso sistema bancário, até logo!")
