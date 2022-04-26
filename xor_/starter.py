from pwn import *
cadena = "label"

cadena = xor(cadena,13).decode()
print(cadena)

