'''Ejemplo estructurada'''

from datetime import datetime

# Solicitar la cantidad de estudiantes
cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

# Lista para almacenar los datos de los estudiantes
estudiantes = []

# Recolección de datos de los estudiantes
for _ in range(cantidad_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota1 = float(input(f"Ingrese la primera nota de {nombre}: "))
    nota2 = float(input(f"Ingrese la segunda nota de {nombre}: "))
    estudiantes.append((nombre, nota1, nota2))

# Variables para rastrear el promedio más alto y el número de aprobados
PROMEDIO_MAS_ALTO = 0
NOMBRE_MEJOR_ESTUDIANTE = ""
CANTIDAD_APROBADOS = 0

# Calcular y mostrar el promedio de cada estudiante
print("\nPromedios de los estudiantes:")
for estudiante in estudiantes:
    nombre, nota1, nota2 = estudiante
    promedio = (nota1 + nota2) / 2
    print(f"{nombre}: Promedio = {promedio:.2f}")
    # Verificar si es el promedio más alto
    if promedio > PROMEDIO_MAS_ALTO:
        PROMEDIO_MAS_ALTO = promedio
        NOMBRE_MEJOR_ESTUDIANTE = nombre

    # Contar estudiantes aprobados (promedio >= 6)
    if promedio >= 6:
        CANTIDAD_APROBADOS += 1

# Imprimir resultados finales
print("\nResultados:")
print(
    f"El estudiante con el promedio más alto es : {NOMBRE_MEJOR_ESTUDIANTE} "
    f"con un promedio de {PROMEDIO_MAS_ALTO:.2f}"
)
print(f"Número de estudiantes con promedio mayor o igual a 6: {CANTIDAD_APROBADOS}")

# Verificar si la fecha actual es 25 de diciembre
fecha_actual = datetime.now()
if fecha_actual.day == 25 and fecha_actual.month == 12:
    print("¡Feliz Navidad!")
