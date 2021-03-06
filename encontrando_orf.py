# -*- coding: utf-8 -*-
"""encontrando ORF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zpTX1RX0oCazeBxzuGd-OcmM-oeh9Jb3

#Exercício 3 de Strings
A sequência abaixo representa um pré-mRNA, ou seja, um RNA não processado, no qual os íntrons não foram removidos. Essa sequência possui um éxon, que começa com AUG e termina com um stop códon UAG. Determine em que posições começam os códons de iniciação e parada e retorne o éxon dessa sequência
"""

seqRNA='AAAUUUAUGUUCCCUUUGGGUGGGCCCGGGAAAUAGUUCUUGUUUAAAUUC'

"""Posições dos códons de iniciação e terminação"""

começo = seqRNA.find('AUG')
final = seqRNA.find('UAG')

começo

final

"""Imprimindo a ORF"""

exon = seqRNA[começo:final]

print(f'A região codificadora é {exon}')