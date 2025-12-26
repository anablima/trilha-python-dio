"""
Exemplos de criação e uso de tipos de data e hora em Python:
- date: somente data (ano, mês, dia)
- datetime: data e hora
- time: somente hora (hora, minuto, segundo)
"""

# Importa as classes 'date', 'datetime' e 'time' do módulo datetime
from datetime import date, datetime, time

# Cria uma data específica (ano, mês, dia)
data = date(2023, 7, 10)
# Imprime a data criada (formato ISO: YYYY-MM-DD)
print(data)
# Obtém e imprime a data atual do sistema
print(date.today())

# Cria um datetime com a data especificada
# Observação: sem argumentos de hora, assume 00:00:00 por padrão
data_hora = datetime(2023, 7, 10)
# Imprime o datetime criado (data + hora)
print(data_hora)
# Obtém e imprime a data e hora atuais do sistema
print(datetime.today())

# Cria um objeto 'time' com hora, minuto e segundo
hora = time(10, 20, 0)
# Imprime a hora criada
print(hora)
