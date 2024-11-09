'''Ejercicio con FOR para cada tipo de dato en Python'''

# 1. LISTA: Recorrer una lista de números y sumar todos los elementos
# Lista de números
numeros = [10, 20, 30, 40, 50]

# Inicializamos la variable para almacenar la suma
SUMA = 0

# Recorremos la lista con un ciclo FOR
for numero in numeros:
    SUMA += numero  # Sumamos cada número a la variable suma

print("Suma de los números en la lista:", SUMA)  # Debería mostrar: 150
# 📝 Aquí se muestra cómo sumar los elementos de una lista usando FOR.

# 2. TUPLA: Recorrer una tupla de palabras y convertir cada palabra en
# mayúsculas
# Tupla de palabras
palabras = ("python", "es", "genial", "y", "poderoso")

# Recorremos la tupla con un ciclo FOR y convertimos cada palabra en mayúsculas
for palabra in palabras:
    print(palabra.upper())  # Imprimimos la palabra en mayúsculas
# 📝 Mostramos cómo recorrer una tupla y modificar la forma de cada elemento
# (convertir a mayúsculas).

# 3. CONJUNTO: Recorrer un conjunto de nombres y verificar si un nombre
# específico está presente
# Conjunto de nombres
nombres = {"Andrés", "Katherin", "Juan", "Ana", "Camila"}

# Nombre a buscar
NOMBRE_A_BUSCAR = "Katherin"

# Recorremos el conjunto con un ciclo FOR y verificamos si el nombre está
# presente
for nombre in nombres:
    if nombre == NOMBRE_A_BUSCAR:
        print(f"{NOMBRE_A_BUSCAR} se encuentra en el conjunto.")
        break  # Salimos del ciclo una vez que encontramos el nombre
else:
    print(f"{NOMBRE_A_BUSCAR} no está en el conjunto.")
# 📝 El ciclo FOR aquí se usa para buscar un nombre en un conjunto, el cual es
# desordenado.

# 4. DICCIONARIO: Recorrer un diccionario de usuarios con su rol y mostrar un
# mensaje para cada usuario
# Diccionario de usuarios y sus roles
usuarios_roles = {
    'Andrés': 'Administrador',
    'Katherin': 'Psicóloga',
    'Juan': 'Desarrollador',
    'Ana': 'Diseñadora',
    'Camila': 'Project Manager'
}

# Recorremos el diccionario con un ciclo FOR
for usuario, rol in usuarios_roles.items():
    print(f"{usuario} tiene el rol de {rol}.")
# 📝 Aquí mostramos cómo recorrer un diccionario y acceder tanto a las claves
# como a los valores.

# 5. FROZENSET: Recorrer un frozenset de números y verificar si un número
# específico está presente
# Frozenset de números
numeros_inmutables = frozenset([1, 2, 3, 4, 5])

# Número a verificar
NUM_A_VERIFICAR = 3

# Recorremos el frozenset con un ciclo FOR
for numero in numeros_inmutables:
    if numero == NUM_A_VERIFICAR:
        print(f"{NUM_A_VERIFICAR} está presente en el frozenset.")
        break  # Salimos del ciclo una vez que encontramos el número
else:
    print(f"{NUM_A_VERIFICAR} no está en el frozenset.")
# 📝 El ciclo FOR se usa para recorrer un frozenset y verificar la presencia
# de un número.
