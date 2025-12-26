from dataclasses import dataclass
from typing import Self


# Modelos de domínio usando `dataclass` para reduzir boilerplate.
# `Cliente` representa atributos comuns; PF/PJ especializam com campos próprios.
@dataclass
class Cliente:
    email: str
    telefone: str
    status: str

    def __str__(self) -> str:
        # Constrói uma apresentação amigável percorrendo atributos do objeto.
        # Substitui underscores por espaços e capitaliza o nome do campo.
        texto = ""
        for campo, valor in self.__dict__.items():
            campo = campo.replace("_", " ").capitalize()
            texto += f"{campo}: {valor}\n"
        return texto


@dataclass
class PessoaFisica(Cliente):
    nome: str
    cpf: str
    renda_mensal: float

    @classmethod
    def converter_objeto_bd(cls, objeto_db: dict) -> Self:
        # Converte um dicionário vindo do banco (Row/dict) em instância de PF.
        # Espera chaves compatíveis com nomes dos campos.
        return cls(
            email=objeto_db["email"],
            telefone=objeto_db["telefone"],
            status=objeto_db["status"],
            nome=objeto_db["nome"],
            cpf=objeto_db["cpf"],
            renda_mensal=objeto_db["renda_mensal"],
        )


@dataclass
class PessoaJuridica(Cliente):
    nome_fantasia: str
    cnpj: str
    faturamento_anual: float

    @classmethod
    def converter_objeto_bd(cls, objeto_db: dict) -> Self:
        # Converte um dicionário vindo do banco em instância de PJ.
        return cls(
            email=objeto_db["email"],
            telefone=objeto_db["telefone"],
            status=objeto_db["status"],
            nome_fantasia=objeto_db["nome_fantasia"],
            cnpj=objeto_db["cnpj"],
            faturamento_anual=objeto_db["faturamento_anual"],
        )
