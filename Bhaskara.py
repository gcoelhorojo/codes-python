#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


a = float(input('Qual o valor de a? '))
b = float(input('Qual o valor de b? '))
c = float(input('Qual o valor de c?'))

delta = b**2 - 4 * a * c

if delta == 0:
    raiz1 =  (-b + math.sqrt(delta)) / (2 * a)
    print('A unica raiz é: ',raiz1)
else:
    if delta < 0:
        print('Sinto muito, essa equação não possui raizes reais...')
    else:    
        raiz1 =  (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print('A primeira raiz é: ', raiz1)
        print('A segunda raiz é: ', raiz2)


# In[ ]:




