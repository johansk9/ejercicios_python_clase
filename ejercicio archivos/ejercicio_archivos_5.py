try:
    with open("origen.txt", "r") as archivo_origen:
        contenido = archivo_origen.read()
    
    with open("destino.txt", "w") as archivo_destino:
        archivo_destino.write(contenido)
    
    print("El contenido de 'origen.txt' ha sido copiado a 'destino.txt'.")
except FileNotFoundError:
    print("El archivo 'origen.txt' no se encuentra en el directorio.")
except Exception as e:
    print(f"Se produjo un error: {e}")
