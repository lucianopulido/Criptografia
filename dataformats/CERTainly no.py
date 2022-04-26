#!/usr/bin/env python
# coding: utf-8

# In[3]:


from Crypto.PublicKey import RSA
##Convertir Archivo .der a .pem con OPENSSL 
## openssl x509 -inform DER -outform PEM -in ..\2048b-rsa-example-cert.der -out ...\2048b-rsa-example-cert.pem
with open('2048b-rsa-example-cert.pem','r') as key_file:
    key = RSA.import_key(key_file.read())
    print(type(key))
    print(key.n)


# In[ ]:




