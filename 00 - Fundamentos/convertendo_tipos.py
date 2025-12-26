"""
Conversões de tipos e operadores de divisão:
- `int(x)`: converte para inteiro (trunca floats, parseia strings numéricas).
- `float(x)`: converte para ponto flutuante.
- `str(x)`: converte para string.
- `/` divisão real; `//` divisão inteira (floor).
"""

# Conversões para inteiro e float
print(int(1.97348728))  # truncamento: 1
print(int("10"))        # parse de string: 10
print(float("10.10"))   # parse de string: 10.1
print(float(100))        # inteiro para float: 100.0

# Conversão para string e inspeção de tipos
valor = 10
valor_str = str(valor)
print(type(valor))       # <class 'int'>
print(type(valor_str))   # <class 'str'>

# Divisão real vs divisão inteira
print(100 / 2)           # 50.0 (float)
print(100 // 2)          # 50 (inteiro)
