#zona de funciones
def capturar_datos():
    total_productos = 0
    suma_calificaciones = 0
    excelentes = 0

    cantidad = int(input("¿Cuántos productos desea calificar?: "))

    for i in range(cantidad):
        calificacion = int(input("Calificación (1 a 5): "))

        while calificacion < 1 or calificacion > 5:
            print("Calificación inválida.")
            calificacion = int(input("Calificación (1 a 5): "))

        total_productos = total_productos + 1
        suma_calificaciones = suma_calificaciones + calificacion

        if calificacion == 5:
            excelentes = excelentes + 1

    datos = (total_productos, suma_calificaciones, excelentes)
    return datos


def analizar_datos(datos):
    total_productos, suma_calificaciones, excelentes = datos

    if total_productos != 0:
        promedio = suma_calificaciones / total_productos
    else:
        promedio = 0

    return promedio


def mostrar_resultados(datos, promedio):
    total_productos, suma_calificaciones, excelentes = datos

    print("\n--- RESULTADOS ---")
    print("Total de productos:"+ str( total_productos))
    print("Suma de calificaciones:"+ str( suma_calificaciones))
    print("Productos excelentes (5 estrellas):"+ str (excelentes))
    print("Promedio de calificación:" + str( promedio))


# codigo principal
datos = capturar_datos()
promedio = analizar_datos(datos)
mostrar_resultados(datos, promedio)
