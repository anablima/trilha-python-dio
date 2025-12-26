"""
Exemplos de uso de timedelta e operações com data/hora:
- Criação de intervalos de tempo com timedelta
- Soma/subtração de datas e datetimes
- Extração de partes (date/time) e diferenças
"""

# Importa tipos principais para trabalhar com datas e horas
from datetime import date, datetime, timedelta

# Tipo de carro selecionado (P: pequeno, M: médio, G: grande)
tipo_carro = "M"  # P, M, G

# Tempos estimados em DIAS para cada tipo (valores ilustrativos)
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

# Data/hora atuais do sistema
data_atual = datetime.now()

# Usa timedelta para ajustar a data estimada conforme o tipo de carro
# Observação: abaixo está sendo feita SUBTRAÇÃO; normalmente uma previsão de término futura
# usaria ADIÇÃO com timedelta (ex.: data_estimada = data_atual + timedelta(days=...))
if tipo_carro == "P":
    data_estimada = data_atual - timedelta(days=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual - timedelta(days=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual - timedelta(days=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

# Exemplo: ontem (data de hoje menos 1 dia)
print(date.today() - timedelta(days=1))

# Subtrai 1 hora de um datetime específico
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
# Imprime apenas a parte de hora (HH:MM:SS)
print(resultado.time())

# Imprime somente a data (YYYY-MM-DD) do momento atual
print(datetime.now().date())
