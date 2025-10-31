# Função que recebe argumentos posicionais e nomeados para exibir um poema com metadados
def exibir_poema(data_extenso, *args, **kwargs):
    # Construindo a mensagem do poema
    texto = "\n".join(args)
    # Construindo os metadados a partir dos argumentos nomeados
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    # Combinando tudo em uma única mensagem
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    # Exibindo a mensagem final
    print(mensagem)

# Chamando a função com um poema e seus metadados
exibir_poema(
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)
