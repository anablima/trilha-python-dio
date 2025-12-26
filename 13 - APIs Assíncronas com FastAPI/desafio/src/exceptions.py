class AccountNotFoundError(Exception):
    # Erro de domínio para conta inexistente
    pass


class BusinessError(Exception):
    # Erros de regra de negócio (ex.: saldo insuficiente)
    pass
