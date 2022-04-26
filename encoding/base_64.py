import base64

cadena_hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
cadena_bytes = bytes.fromhex(cadena_hex)
cadena_base64 = base64.b64encode(cadena_bytes).decode()
print(cadena_base64)
