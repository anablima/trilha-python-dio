"""
Exemplo de uso de timezone nativo (sem pytz):
- Cria objetos de fuso horário com deslocamentos fixos usando timezone + timedelta
- Obtém datetimes cientes de fuso (timezone-aware) para Oslo (+02:00) e São Paulo (-03:00)

Observação: timezone com deslocamento fixo não adapta automaticamente para DST.
Para regras completas de fuso e horário de verão, use bibliotecas como `pytz` ou `zoneinfo` (Python 3.9+).
"""

from datetime import datetime, timedelta, timezone

# Fuso horário com offset de +2 horas (aproximação de Europe/Oslo)
data_oslo = datetime.now(timezone(timedelta(hours=2)))

# Fuso horário com offset de -3 horas (aproximação de America/Sao_Paulo)
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

# Imprime os datetimes com seus respectivos offsets
print(data_oslo)
print(data_sao_paulo)
