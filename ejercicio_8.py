#zona de funciones
def capturar_datos():
    edad = int(input("Ingrese la edad del participante (0 para finalizar): "))
    return edad


def analizar_datos(edad_inicial):
    publico_objetivo = 0
    suma_edades = 0
    cantidad_personas = 0
    registro = ""

    edad = edad_inicial

    while edad != 0:
        cantidad_personas = cantidad_personas + 1
        suma_edades = suma_edades + edad

        if edad >= 25 and edad <= 45:
            publico_objetivo = publico_objetivo + 1
            registro = registro + "Edad dentro del público objetivo: " + str(edad) + "\n"
        else:
            registro = registro + "Edad fuera del rango: " + str(edad) + "\n"

        edad = int(input("Ingrese la edad del participante (0 para finalizar): "))

    
    if cantidad_personas > 0:
        promedio = suma_edades / cantidad_personas
    else:
        promedio = 0

    resultado = (
        "--- RESULTADOS DE LA ENCUESTA ---\n"
        "Total de participantes: " + str(cantidad_personas) + "\n"
        "Público objetivo (25-45): " + str(publico_objetivo) + "\n"
        "Promedio de edad: " + str(promedio) + "\n\n"
        "DETALLES REGISTRADOS:\n" + str(registro) 
    )

    return resultado


def mostrar_resultados(resultado):
    print(resultado)
   


# codigo principal
edad_inicial = capturar_datos()
resultado = analizar_datos(edad_inicial)
mostrar_resultados(resultado)
