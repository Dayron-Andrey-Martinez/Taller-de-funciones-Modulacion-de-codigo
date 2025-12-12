#zona de funciones
def capturar_datos():
    venta = float(input("Ingrese ventas del vendedor (0 o negativo para finalizar): "))
    return venta


def analizar_datos(venta_inicial):
    meta = 5000
    total_vendedores = 0
    cumplidos = 0
    registro = ""

    venta = venta_inicial

    while venta > 0:
        total_vendedores = total_vendedores + 1

        if venta >= meta:
            cumplidos = cumplidos + 1
            registro = registro + "Vendedor " + str(total_vendedores) + " cumplió la meta (" + str(venta) + ")\n"
        else:
            registro = registro + "Vendedor " + str(total_vendedores) + " NO cumplió (" + str(venta) + ")\n"

        venta = float(input("Ingrese ventas del vendedor (0 o negativo para finalizar): "))

   
    resultado = (
        "--- REPORTE DE METAS DE VENTAS ---\n"
        "Total de vendedores procesados: " + str(total_vendedores) + "\n"
        "Vendedores con meta cumplida: " + str(cumplidos) + "\n\n"
        "REGISTRO DETALLADO:\n" + str(registro) 
       
    )

    return resultado


def mostrar_resultados(resultado):
    print(resultado)
    

# codigo principal
venta_inicial = capturar_datos()
resultado = analizar_datos(venta_inicial)
mostrar_resultados(resultado)
