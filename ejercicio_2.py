# zona de funciones
def capturar_datos():
    codigo_correcto = "SR.DAYRON"
    accesos_permitidos = 0
    accesos_denegados = 0
    mensaje_accesos = ""

    while True:
        codigo = input("Ingrese código o escriba SALIR: ")

        if codigo == "SALIR":
            break

        if codigo == codigo_correcto:
            accesos_permitidos = accesos_permitidos + 1
            mensaje_accesos = mensaje_accesos + "Acceso permitido para " + codigo + "\n"
        else:
            accesos_denegados = accesos_denegados + 1
            mensaje_accesos = mensaje_accesos + "Acceso denegado para " + codigo + "\n"

    datos = (accesos_permitidos, accesos_denegados, mensaje_accesos)
    return datos


def analizar_datos(datos):
    accesos_permitidos, accesos_denegados, mensaje_accesos = datos

   
    total_intentos = accesos_permitidos + accesos_denegados

    return total_intentos


def mostrar_resultados(datos, total_intentos):
    accesos_permitidos, accesos_denegados, mensaje_accesos = datos

    print("\n--- REGISTRO DE ACCESOS ---")
    print(mensaje_accesos)

    print("--- RESUMEN ---")
    print("Accesos permitidos:"+ str(accesos_permitidos))
    print("Accesos denegados :"+ str(accesos_denegados))
    print("Intentos totales  :"+ str(total_intentos))


# codigo principal
datos = capturar_datos()
total_intentos = analizar_datos(datos)
mostrar_resultados(datos, total_intentos)
