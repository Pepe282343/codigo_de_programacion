def calcular_objetivo_ml(peso, actividad):  # Esta función calcula la cantidad de agua recomendada por día

    base = peso * 35

    if actividad == "bajo":
        return base * 0.9

    elif actividad == "medio":
        return base

    elif actividad == "alto":
        return base * 1.1   
    #donde se guarda el valor que retorna la funcion
    
def estado_hidratacion(consumo, objetivo):  # Esta función compara el agua consumida con el objetivo diario

    if consumo < objetivo:
        return "Te falta tomar más agua."

    elif consumo == objetivo:
        return "Llegaste al objetivo."

    else:
        return "Superaste el objetivo."


personas = []

continuar = "si"
while continuar == "si":# Esta parte del programa permite ingresar los datos de varias personas,calcular su consumo recomendado de agua y guardar la información.
    try:
        peso = float(input("Ingrese su peso en kg: "))

        actividad = input(
            "Ingrese actividad (bajo, medio, alto): "
        ).lower()

        consumo = float(
            input("Ingrese agua consumida en ml: ")
        )

        objetivo = calcular_objetivo_ml(peso, actividad)

        estado = estado_hidratacion(consumo, objetivo)

        print("\nObjetivo:", objetivo, "ml")
        print("Estado:", estado)

        persona = {
            "peso": peso,
            "actividad": actividad,
            "consumo": consumo,
            "objetivo": objetivo
        }

        personas.append(persona)

    except ValueError:
        print("Error: dato inválido")

    continuar = input(
        "\n¿Desea cargar otra persona? "
    ).lower()


print("\n--- RESUMEN ---")

for persona in personas:

    print(persona)