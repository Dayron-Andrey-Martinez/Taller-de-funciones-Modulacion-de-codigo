#zona de funciones
def capturar_datos():
    entrada = input("Ingrese cantidad de unidades del lote o 'STOP' para finalizar: ")
    return entrada


def analizar_datos(entrada):
    cantidad = int(entrada)

    defectuosos = 0
    ok = 0
    registro_fallos = ""
    registro_ok = ""

    for i in range(1, cantidad + 1):
        estado = input("Unidad " + str(i) + " (D=defectuosa / O=OK): ")

        if estado == "D":
            defectuosos = defectuosos + 1
            registro_fallos = registro_fallos + "Fallo en unidad " + str(i) + "\n"

        elif estado == "O":
            ok = ok + 1
            registro_ok = registro_ok + "Unidad " + str(i) + " OK\n"

        else:
            print("⚠ Estado inválido. No se registra.")

    total = defectuosos + ok
    porcentaje = (defectuosos * 100) / total


    resultado = (
        "--- RESULTADOS DEL LOTE ---\n"
        "Unidades OK: " + str(ok) + "\n"
        "Unidades defectuosas: " + str(defectuosos) + "\n"
        "Porcentaje defectuoso: " + str(porcentaje) + "%\n\n"
        "REGISTRO DE FALLOS:\n" + str(registro_fallos) +
        "REGISTRO DE UNIDADES OK:\n" + str(registro_ok) 
        
    )

    return resultado


def mostrar_resultados(resultado):
    print(resultado)
   


# Codigo principal
while True:
    entrada = capturar_datos()

    if entrada == "STOP":
        break

    resultado = analizar_datos(entrada)
    mostrar_resultados(resultado)
