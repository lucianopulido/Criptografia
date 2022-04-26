from pwn import *  # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import *

r = remote('socket.cryptohack.org', 13377, level='debug')


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def decryptor(tipo, cadena, cadenaDecodificada):
    if tipo == "base64":
        cadenaDecodificada = base64.b64decode(cadena).decode()
    if tipo == "rot13":
        cadenaDecodificada = codecs.decode(cadena, 'rot_13')
    if tipo == "hex":
        cadenaDecodificada = codecs.decode(cadena, 'hex').decode()
    if tipo == "bigint":
        cadenaDecodificada = codecs.decode(cadena[2:], 'hex').decode()
    if tipo == "utf-8":
        for numero in received["encoded"]:
            cadenaDecodificada += chr(numero)
    return cadenaDecodificada


received = json_recv()

print("Received type: ", received["type"])
print("Received encoded value: ", received["encoded"])
flag = ""
while not 'flag' in received:
    cadenaDecodificada = ""
    cadenaCodificada = received["encoded"]
    tipo = received["type"]
    cadenaDecodificada = decryptor(tipo, cadenaCodificada, cadenaDecodificada)

    print("Cadena decodificada:", cadenaDecodificada)
    to_send = {
        "decoded": cadenaDecodificada
    }
    json_send(to_send)
    received = json_recv()

print("Flag:", flag)
