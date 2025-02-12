def buscar_palabra_en_archivo(archivo, palabra):
    try:
        with open(archivo, "r") as file:
            contenido = file.read()
            conteo = contenido.lower().count(palabra.lower())
            return conteo
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encuentra en el directorio.")
        return 0
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
        return 0

palabra = input("Introduce la palabra que deseas buscar: ")

conteo_palabra = buscar_palabra_en_archivo("articulo.txt", palabra)

if conteo_palabra > 0:
    print(f"La palabra '{palabra}' aparece {conteo_palabra} veces en el archivo.")
else:
    print(f"La palabra '{palabra}' no se encuentra en el archivo.")
