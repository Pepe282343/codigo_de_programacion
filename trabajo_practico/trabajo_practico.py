def calcular_objetivo_ml(peso, actividad):

    base = peso * 35

    if actividad == "bajo":
        return base * 0.9

    elif actividad == "medio":
        return base

    elif actividad == "alto":
        return base * 1.1


def estado_hidratacion(consumo, objetivo):

    if consumo < objetivo:
        return "Te falta tomar más agua."

    elif consumo == objetivo:
        return "Llegaste al objetivo."

    else:
        return "Superaste el objetivo."


personas = []

continuar = "si"

while continuar == "si":

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