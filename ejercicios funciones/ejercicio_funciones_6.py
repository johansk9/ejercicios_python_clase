def promedio(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

resultado1 = promedio(700, 20, 30)
resultado2 = promedio(5, 15)
resultado3 = promedio(100, 200, 300, 400, 500)

print("Promedio de 700, 20, 30:", resultado1)
print("Promedio de 5, 15:", resultado2)
print("Promedio de 100, 200, 300, 400, 500:", resultado3)
