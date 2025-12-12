# zona de funciones

def capturar_datos():
    saldo_inicial = 2600
    print("Saldo inicial:" + str(saldo_inicial))

    cantidad = int(input("¿Cuántas transacciones desea registrar?: "))

    paquete = str(saldo_inicial) + "#" + str(cantidad)
    return paquete


def separar(paquete):
    saldo_txt = ""
    cantidad_txt = ""
    cambio = False

    for c in paquete:
        if c == "#":
            cambio = True
        elif cambio == False:
            saldo_txt = saldo_txt + c
        else:
            cantidad_txt = cantidad_txt + c

    saldo = float(saldo_txt)
    cantidad = int(cantidad_txt)

 
    paquete_convertido = str(saldo) + "#" + str(cantidad)
    return paquete_convertido


def analizar_datos(paquete):
    paquete_convertido = separar(paquete)
    saldo_txt = ""
    cantidad_txt = ""
    cambio = False

    for c in paquete_convertido:
        if c == "#":
            cambio = True
        elif cambio == False:
            saldo_txt = saldo_txt + c
        else:
            cantidad_txt = cantidad_txt + c

    saldo = float(saldo_txt)
    cantidad = int(cantidad_txt)

    transacciones_validas = 0

    for i in range(cantidad):
        tipo = input("Ingrese tipo de transacción (D-depósito / R-retiro / FIN): ")

        if tipo == "FIN":
            break

        monto = float(input("Ingrese monto de la transacción: "))

        if tipo == "D":
            saldo = saldo + monto
            transacciones_validas = transacciones_validas + 1

        elif tipo == "R":
            if saldo - monto >= 0:
                saldo = saldo - monto
                transacciones_validas = transacciones_validas + 1
            else:
                print(" No se puede retirar, saldo insuficiente.")
        else:
            print(" Tipo inválido.")

    paquete_salida = str(saldo) + "#" + str(transacciones_validas)
    return paquete_salida


def mostrar_resultados(paquete_salida):
 
    saldo_txt = ""
    trans_txt = ""
    cambio = False

    for c in paquete_salida:
        if c == "#":
            cambio = True
        elif cambio == False:
            saldo_txt = saldo_txt + c
        else:
            trans_txt = trans_txt + c

    saldo = float(saldo_txt)
    transacciones = int(trans_txt)

    print("\n--- RESULTADOS ---")
    print("Balance final del día: " + str(saldo))
    print("Total de transacciones válidas: " + str(transacciones))


# código principal
paquete = capturar_datos()
paquete_salida = analizar_datos(paquete)
mostrar_resultados(paquete_salida)
