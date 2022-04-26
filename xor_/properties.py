from pwn import *
cadena1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
cadena2 = "dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
cadena3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
cadena4 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
cadena1 = bytes.fromhex(cadena1)
cadena2 = bytes.fromhex(cadena2)
cadena3 = bytes.fromhex(cadena3)
cadena4 = bytes.fromhex(cadena4)
cadena4 = xor(cadena4,cadena3,cadena1)
print(cadena4)
