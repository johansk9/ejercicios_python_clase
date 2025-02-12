precio = float(input("Ingresa el precio del producto: "))

if precio > 1000:
    descuento = precio * 0.10
    precio_final = precio - descuento
    print(f"Se aplicó un descuento del 10%. Precio final: {precio_final:.2f}")
else:
    print(f"El precio final es: {precio:.2f}")
