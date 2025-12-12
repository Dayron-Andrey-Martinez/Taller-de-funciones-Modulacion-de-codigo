#zona de funciones
def capturar_datos():
    horas = int(input("Ingrese horas extra del empleado (negativa para terminar): "))
    return horas


def analizar_datos():
    total_bonificacion = 0
    contador_empleados = 0

    while True:
        horas = capturar_datos()

        if horas < 0:
            resultado = (total_bonificacion, contador_empleados)
            return resultado

        contador_empleados = contador_empleados + 1

        if horas > 5:
            bonificacion = horas * 15
        else:
            bonificacion = horas * 10

        total_bonificacion = total_bonificacion + bonificacion
        print("Bonificación del empleado:", bonificacion)


def mostrar_resultados(resultado):
    total, empleados = resultado
    print("\n--- RESULTADOS ---")
    print("Total pagado en bonificaciones:"+ str(total))
    print("Cantidad de empleados con bonificación:"+str( empleados))


# codigo principal
resultado_final = analizar_datos()
mostrar_resultados(resultado_final)
