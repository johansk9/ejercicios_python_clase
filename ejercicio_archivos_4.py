nombres = ["Johan", "Cheng", "Pedro", "Maria", "Luis"]

try:
    with open("nombres.txt", "w") as archivo:
        for nombre in nombres:
            archivo.write(nombre + "\n")
    print("Los nombres han sido guardados en 'nombres.txt'.")
except Exception as e:
    print(f"Se produjo un error al guardar los nombres en el archivo: {e}")
