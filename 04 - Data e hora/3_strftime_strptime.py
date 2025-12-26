"""
Formatação e parsing de datas/horas com strftime e strptime:
- strftime: formata um datetime em string conforme uma máscara
- strptime: converte (parse) uma string para datetime usando a máscara

Diretivas usadas:
%d (dia), %m (mês), %Y (ano), %a (dia da semana abreviado),
%H (hora 00-23), %M (minutos)
"""

from datetime import datetime

# Obtém o momento atual
data_hora_atual = datetime.now()

# String de data/hora no padrão ISO parcial (ano-mês-dia hora:min)
data_hora_str = "2023-10-20 10:20"

# Máscara de formatação (pt-BR): dia/mês/ano + dia da semana abreviado
mascara_ptbr = "%d/%m/%Y %a"

# Máscara que corresponde ao formato de data_hora_str
mascara_en = "%Y-%m-%d %H:%M"

# Formata o datetime atual conforme a máscara pt-BR
print(data_hora_atual.strftime(mascara_ptbr))

# Converte a string para datetime usando a máscara compatível
data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
# Mostra o tipo do objeto convertido (deve ser datetime)
print(type(data_convertida))
