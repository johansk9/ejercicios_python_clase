persona = {
    "nombre": "Johan",
    "edad": 21,
    "ciudad": "Madrid"
}
print("Diccionario inicial:", persona)

persona["edad"] = 22
print("Diccionario después de cambiar la edad:", persona)

del persona["ciudad"]
print("Diccionario después de eliminar 'ciudad':", persona)
