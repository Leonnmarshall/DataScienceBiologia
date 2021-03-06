# -*- coding: utf-8 -*-
"""Analisando proteínas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jb5Dm68v9yqtRB3sBzNXIFsN2oeQ2vFe

#Exercício 2 de Strings

Abaixo há a representação de duas proteínas. Uma delas é mutante pois teve uma de suas metioninas mutadas para 'leucina' e, portanto, é maior que sua versão normal. Com base nas sequências, calcule:

a) Quanto (%) a proteína mutante é maior que a normal

b) O comprimento de aa's de cada proteína

c) A porcentagem de serina (S) nas duas sequências

Proteínas
"""

#proteinas


protein1 = 'MGTACHMCGYGCYGYGSHSCIOOENNFHEF'

protein2 = 'MCCFOTYOOANLGTACHMCGYGCYGYGSHSCIOOENNFHEF'

"""Calculando a relação de tamanho"""

tamanho1 = len(protein1)

tamanho2 = len(protein2)

razao = ((tamanho2/tamanho1)-1)*100

razao

"""Calculando o comprimento de cada proteína"""

print('O comprimento da proteína 1 é de ',len(protein1),'aas')
print('O comprimento da proteína 2 é de ',len(protein2),'aas')

"""Calculando a porcentagem de serina (S) em cada proteína"""

quantSprot1 = protein1.count('S')
quantAAprot1 = len(protein1)
porcentagemSprot1 = (quantSprot1/quantAAprot1)*100

quantSprot2 = protein2.count('S')
quantAAprot2 = len(protein2)
porcentagemSprot2 = (quantSprot2/quantAAprot2)*100

print('A porcentagem de serina na proteína 1 é de:',round(porcentagemSprot1,2))
print('A porcentagem de serina na proteína 2 é de:',round(porcentagemSprot2,2))