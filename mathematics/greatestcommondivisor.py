def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

numero = gcd(66528,52920)
print(numero)