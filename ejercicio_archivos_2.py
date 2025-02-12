try:
    with open("poema.txt", "r") as archivo:
        lineas = archivo.readlines()
        print(f"El archivo tiene {len(lineas)} líneas.")
except FileNotFoundError:
    print("El archivo 'poema.txt' no se encuentra en el directorio.")
except Exception as e:
    print(f"Se produjo un error al leer el archivo: {e}")
