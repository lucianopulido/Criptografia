from Crypto.PublicKey import RSA

f = open('bruce_rsa.pub', 'r')
public_key = RSA.importKey(f.read())
print(public_key.n)