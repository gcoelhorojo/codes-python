#!/usr/bin/env python
# coding: utf-8

# In[10]:


n = int(input("Digite um número inteiro: "))

soma = 0

while (n != 0):
    resto = n % 10
    n = (n - resto) // 10
    soma = soma + resto

print(soma)


# In[ ]:




