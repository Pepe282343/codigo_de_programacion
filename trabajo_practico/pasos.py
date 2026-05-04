def calcular_objetivo_ml(peso_kg, nivel_actividad)

 
def estado_hidratacion(consumo_ml, objetivo_ml):


personas = []

continuar = "si"

while continuar == "si":

    try:

        peso = float(input("Ingrese su peso en kg: "))

        nivel_actividad = input("Ingrese nivel de actividad: ").lower()

        consumo_hoy = float(input("Ingrese agua consumida en ml: "))

    except ValueError:
        print("Dato inválido")

    continuar = input("¿Desea continuar? ").lower()