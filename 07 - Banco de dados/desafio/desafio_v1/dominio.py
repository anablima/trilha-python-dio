from dataclasses import dataclass


# Camada de domínio (modelos de dados) usando `dataclasses` para simplicidade.
# Essas classes representam entidades de cliente, PF e PJ, com seus atributos.
@dataclass
class Cliente:
    # Contato e status comum a qualquer cliente
    email: str
    telefone: str
    status: str


@dataclass
class PessoaFisica(Cliente):
    # Dados específicos de pessoa física
    nome: str
    cpf: str
    renda_mensal: float


@dataclass
class PessoaJuridica(Cliente):
    # Dados específicos de pessoa jurídica
    nome_fantasia: str
    cnpj: str
    faturamento_anual: float
