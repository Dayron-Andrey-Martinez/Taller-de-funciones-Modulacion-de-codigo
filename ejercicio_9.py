# zona de funciones
def capturar_datos():
    stock_inicial = int(input("Ingrese la cantidad inicial en stock: "))
    return stock_inicial


def analizar_datos(stock_actual):
    mensaje = ""  

    while True:
        venta = int(input("Cantidad vendida hoy (0 para terminar): "))
        if venta == 0:
            mensaje = "Proceso terminado por el usuario. Stock final: "+ str(stock_actual)
            break

        stock_actual = stock_actual - venta
        print("Stock actual:", stock_actual)

        if stock_actual <= 10:
            mensaje = "Aviso de Reposición Urgente. Stock final: "+ str(stock_actual)
            break

    return mensaje   

def mostrar_resultados(mensaje):
    print("\n--- RESULTADOS ---")
    print(mensaje)


# código principal
stock = capturar_datos()
mensaje = analizar_datos(stock)
mostrar_resultados(mensaje)
