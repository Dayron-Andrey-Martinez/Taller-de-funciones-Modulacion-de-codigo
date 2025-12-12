#zona de funciones
def capturar_datos():
    productos = int(input("¿Cuántos productos desea registrar?: "))
    return productos


def analizar_datos(productos):
    subtotal = 0

    for i in range(1, productos + 1):
        print("Producto", i)
        precio = float(input("Precio unitario: "))
        cantidad = int(input("Cantidad: "))

        subtotal = subtotal + (precio * cantidad)

    
    mensaje_descuento = ""
    descuento = 0

    if subtotal > 1000:
        descuento = subtotal * 0.10
        mensaje_descuento = "Se aplicó un 10% de descuento.\n"
    elif subtotal > 500:
        descuento = subtotal * 0.05
        mensaje_descuento = "Se aplicó un 5% de descuento.\n"
    else:
        mensaje_descuento = "No se aplicó ningún descuento.\n"

    total_pagar = subtotal - descuento

    
    resultado = (
        "--- RESUMEN DE COMPRA ---\n"
        "Subtotal: $" + str(subtotal) + "\n"
        + mensaje_descuento +
        "Total a pagar: $" + str(total_pagar) + "\n"
      
    )

    return resultado


def mostrar_resultados(resultado):
    print(resultado)
    


# CODIGO PRINCIPAL.
productos = capturar_datos()
resultado = analizar_datos(productos)
mostrar_resultados(resultado)
