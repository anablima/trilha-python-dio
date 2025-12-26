"""
Exemplo de uso de fuso horário com pytz:
- Obtém o horário atual em diferentes timezones (Europe/Oslo e America/Sao_Paulo)
- Demonstra como criar um objeto timezone e aplicá-lo ao datetime atual
"""

# Importa datetime para trabalhar com data/hora atual
from datetime import datetime

# Biblioteca pytz fornece bancos de dados de timezones e conversões
import pytz

# Cria o timezone para Oslo e obtém o now ciente de fuso (timezone-aware)
data = datetime.now(pytz.timezone("Europe/Oslo"))

# Cria o timezone para São Paulo e obtém o now ciente de fuso (timezone-aware)
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

# Imprime os datetimes com seus respectivos fusos
print(data)
print(data2)
