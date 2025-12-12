#zona de funciones
def capturar_datos():
    lectura = float(input("Ingrese porcentaje de uso de CPU (valor negativo para detener): "))
    return lectura


def analizar_datos(primera_lectura):
    mediciones = 0
    alertas = 0
    registro_alertas = ""

    lectura = primera_lectura

    while lectura >= 0:
        mediciones = mediciones + 1

        if lectura > 90:
            alertas = alertas + 1
            registro_alertas = registro_alertas + "Alerta: Uso Crítico (" + str(lectura) + "%)\n"

        lectura = float(input("Ingrese porcentaje de uso de CPU (valor negativo para detener): "))

    
    resultado = (
        "--- MONITOREO DE CPU ---\n"
        "Total de mediciones: " + str(mediciones) + "\n"
        "Alertas críticas: " + str(alertas) + "\n\n"
        "REGISTRO DE ALERTAS:\n" + str(registro_alertas) 
       
    )

    return resultado


def mostrar_resultados(resultado):
    print(resultado)
   


# PROGRAMA PRINCIPAL
primera_lectura = capturar_datos()
resultado = analizar_datos(primera_lectura)
mostrar_resultados(resultado)
