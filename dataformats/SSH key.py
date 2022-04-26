#!/usr/bin/env python
# coding: utf-8

# In[108]:


from Crypto.PublicKey import RSA

f = open('bruce_rsa.pub', 'r')
public_key = RSA.importKey(f.read())
#Modulo de public_key
print(public_key.n)


# In[ ]:





# In[ ]:





# In[ ]:




