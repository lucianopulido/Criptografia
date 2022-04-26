def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    lista_matriz = []
    for i in range(0, len(text), 4):
        lista_matriz.append(list(text[i:i + 4]))

    return lista_matriz


def matrix2bytes(matrix):
    flag = ""
    for i in matrix:
        for j in i:
            flag += chr(j)
    return flag


matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

# print(bytes2matrix("luciano"))
print(matrix2bytes(matrix))
