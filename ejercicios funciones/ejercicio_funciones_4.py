def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

resultado1 = es_par(10)
resultado2 = es_par(7)
resultado3 = es_par(4)

print("¿El 10 es par?", resultado1)
print("¿El 7 es par?", resultado2)
print("¿El 4 es par?", resultado3)
