try:
    with open("notas.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo 'notas.txt' no se encuentra en el directorio.")
except Exception as e:
    print(f"Se produjo un error al leer el archivo: {e}")
