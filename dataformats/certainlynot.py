from Crypto.PublicKey import RSA

archivo_der = open('rsa-example-cert_.pem', 'r')
private_key = RSA.importKey(archivo_der.read())
print(private_key.n)
