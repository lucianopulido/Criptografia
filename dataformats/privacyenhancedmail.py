from Crypto.PublicKey import RSA

archivo_pem = open('privacy_enhanced_mail.pem', 'r')
private_key = RSA.importKey(archivo_pem.read())
print(private_key.d)

