def imprimir_detalles(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

imprimir_detalles(nombre="Johan", edad=21, ciudad="Madrid")
print()  
imprimir_detalles(titulo="Sr.", nombre="Cheng", profesion="Ingeniero")
print()  
imprimir_detalles(marca="Apple", modelo="iPhone", color="Negro")
