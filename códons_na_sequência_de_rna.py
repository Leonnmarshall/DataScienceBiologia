# -*- coding: utf-8 -*-
"""Códons na sequência de RNA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z-9B98CiPOOjXTPPPYSUW5URIH_x6ORd

#Exercício 3 de condicionais

Escreva um programa em que o usuário deve digitar uma sequência de RNA. O programa deve retornar se há um códon de iniciação (AUG), se há um códon de terminação ou se há os dois ou nenhum.

Entrada do usuário
"""

rna = str(input('Sequência de RNA: '))

"""Condição"""

if 'AUG' in rna:
  if ('UGA' or 'UAA' or 'UAG') in rna:
    print('A sequência possui códon de iniciação e terminação')
  else:
    print('A sequência possui apenas códon de iniciação')
else:
  if ('UGA' or 'UAA' or 'UAG') in rna:
    print('A sequência possui apenas códon de terminação')
  else:
    print('Não possui códon de iniciação nem de terminação')