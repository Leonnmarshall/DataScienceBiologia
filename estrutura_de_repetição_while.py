# -*- coding: utf-8 -*-
"""Estrutura de repetição - while.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1istmkrZj6c7AICiDnM93LXRmiGqq12JA

# Estruturas de repetição - while
"""

numero = 1
while numero < 6:
  print(numero)
  numero += 1
print('---')

numero = 5
while numero > 0:
  print(numero)
  numero -= 1

1 + 2 + 3 + 4 + 5

soma = 0
numero = 1
while numero < 6:
  soma += numero
  numero += 1
print(soma)

numero = 12
while numero < 1 or numero > 10:
  numero = int(input('Digite um número de 1 a 10: '))