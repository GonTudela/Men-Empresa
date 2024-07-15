import random
import statistics
import csv
Trabajadores = ["Juan Perez", "María Garcia", "Carlos López", "Ana Martínez", "Pedro Rodriguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Franciasco Díaz", "Elena Fernandez"]


def AsignarSueldo():
    sueldos = []
    for i in range(10):
        sueldo = random.randint(300000, 2500001)
        sueldos.append(sueldo)
        return sueldos
    
def ClasificarSueldo(sueldos):
    sueldos.sort()
    return sueldos

def VerEstadisticas(sueldos):

    sueldo_bajo = min(sueldos)
    sueldo_alto = max(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    mediageometrica = statistics.geometric_mean(sueldos)
    return sueldo_bajo, sueldo_alto, promedio, mediageometrica


def ReporteSueldos(Trabajadores,sueldos):
    with open("reporte_sueldos.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["Trabajador","Sueldo","Descuento Salud","Descuento AFP","SueldoNeto"])
        for i in range(len(Trabajadores)):
            descuento_salud = sueldos[i] * 0.07
            descuento_AFP = sueldos[i] * 0.12
            sueldo_neto = sueldos[i] - (descuento_salud + descuento_AFP)
            writer.writerow([Trabajadores[i], sueldos[i], descuento_salud,descuento_AFP,sueldo_neto])


while True:
    print("Bienvenido, ¿Qué desea hacer?")
    print("1. Asignar Sueldos")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de Sueldos")
    print("5. Salir del programa")
    op = int(input("Ingrese su opción: "))
    try:
        if op == 1:
            sueldos = AsignarSueldo()
            print("Sueldos asignados de manera exitosa")
        elif op == 2:
            sueldos_clasificados = ClasificarSueldo(sueldos)
            print(f"Sus sueldos clasificados son estos: {sueldos_clasificados}")
        elif op == 3:
            sueldo_bajo, sueldo_alto, promedio, medidageometrica = VerEstadisticas(sueldos)
            print(f"Sueldo más bajo: ${sueldo_bajo}")
            print(f"Sueldo más alto: ${sueldo_alto}")
            print(f"promedio de sueldos: ${medidageometrica}")
        elif op == 4:
            ReporteSueldos(Trabajadores,sueldos)
            print("Generando reporte de sueldos...")
            print(ReporteSueldos)
        elif op == 5:
            print("Finalizando programa...")
            print("Programa desarrollado por: Gonzalo Tudela")
            print("Rut: 21.748.056-6")
            break
        else:
            print("Opcion no valida")
    except ValueError:
        print("Opcion no valida")



