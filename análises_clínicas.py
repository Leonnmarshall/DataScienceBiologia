# -*- coding: utf-8 -*-
"""Análises clínicas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ioTZMu3IQPNnHE3MXiFiE37SVqXaetRJ

#Exercício 2 de condicionais

Faça um programa que pergunte a um individuo do sexo masculino três parâmetros hematológicos, sendo estes: hemácias, hemoglobina e hematócrito. Cada parâmetro terá um status (normal ou alterado). Para estar normal, hemácias deve estar entre 4,5 e 5,5; para hemoglobina, deve estar entre 13 e 17; para o hematócrito, deve estar entre 40 e 50. Caso contrário, o status é considerado alterado. No final, o programa deve imprimir uma frase para cada status, dizendo se está normal ou alterado.

Condição
"""

hemacias = float(input('Hemácias (x10^12/L): '))
if hemacias < 4.5 or hemacias > 5.5:
  statusHemacias = 'alterado'
else:
  statusHemacias = 'normal'
hemoglobina = float(input('Hemoglobina (g/dL): '))
if hemoglobina < 13 or hemoglobina > 17:
  statusHemoglobina = 'alterado'
else:
  statusHemoglobina = 'normal'
hematocrito = float(input('Hematocrito (%): '))
if hematocrito < 40 or hematocrito > 50:
  statusHematocrito = 'alterado'
else:
  statusHematocrito = 'normal'

"""Imprimindo dados na tela"""

print(f'Nível de hemácias: {statusHemacias}')
print(f'Nível de hemoglobina: {statusHemoglobina}')
print(f'Nível de hematocrito: {statusHematocrito}')