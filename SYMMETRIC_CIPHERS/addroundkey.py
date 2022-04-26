from pwn import *


def matrix2bytes(matrix):
    flag = ""
    for i in matrix:
        for j in i:
            flag += (j)
    return flag


def add_round_key(s, k):
    i = 0
    j = 0
    matriz_resultado = []
    lista_aux = []
    while i < len(s):
        while j < len(k):
            lista_aux.append((xor(s[i][j], k[i][j])).decode())
            j += 1
        matriz_resultado.append(lista_aux)
        lista_aux = []
        i += 1
        j = 0

    return matriz_resultado


state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

matriz_resultado = add_round_key(state, round_key)
print(matrix2bytes(matriz_resultado))
