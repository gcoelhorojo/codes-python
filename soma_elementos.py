#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def soma_elementos(lista):
    l = lista
    soma = 0
    for i in range(len(l)):
        soma += l[i]
    return soma

l = []
while True:
    x = int(input('Digite um numero, quando quiser parar, digite 0: '))
    if x == 0:
        break
    l.append(x)

l = soma_elementos(l)
print (l)


# In[ ]:





# In[ ]:




