#!/usr/bin/env python
# coding: utf-8

# In[7]:


def retangulo(largura, altura): 
    for _ in range(altura): 
        print('#' * largura) 

while True: 
    largura = int(input("\nColoque a largura: "))
    altura = int(input("Coloque a altura: "))
    retangulo(largura, altura)
    break


# In[ ]:





# In[ ]:




