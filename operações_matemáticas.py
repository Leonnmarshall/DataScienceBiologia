# -*- coding: utf-8 -*-
"""Operações Matemáticas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x7C9h_g9oMaKQqfx63PIxZFgTAuus9RI

# Operações matemáticas

## Operações matemáticas
"""

a = 5
b = 3
print(a, b)

a + b

print('A soma é', a + b)

print('A subtração é', a - b)

print('A divisão é', a / b)

print('A multiplicação é', a * b)

print('O resto da divisão é', 10 % 3)

5 * 5 * 5 * 5

print('5 elevado a 4 é', 5**4)

import math
math.sqrt(81)

"""## Arredondamento"""

casos_doenca = 134
numero_habitantes = 34432
casos_por_habitante = casos_doenca / numero_habitantes
print(casos_por_habitante)

round(casos_por_habitante, 6)

print('O número de casos por habitante é de', round(casos_por_habitante, 4))