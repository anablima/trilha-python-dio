# Importa functools para preservar metadados da função original
import functools


# Função decoradora que preserva informações da função decorada
def meu_decorador(funcao):
    # @functools.wraps copia metadados da função original para o envelope
    # Isso mantém __name__, __doc__, __module__, etc. da função original
    # Sem isso, envelope.__name__ seria "envelope" ao invés de "ola_mundo"
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        # Executa a função original com os argumentos recebidos
        funcao(*args, **kwargs)

    # Retorna a função envelope com os metadados preservados
    return envelope


# Aplica o decorador à função
@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")


# Imprime o nome da função
# Graças ao @functools.wraps, imprime "ola_mundo" ao invés de "envelope"
# Isso é importante para debugging e introspecção de código
print(ola_mundo.__name__)
