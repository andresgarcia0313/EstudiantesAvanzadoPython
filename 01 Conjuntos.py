# 1. LISTA de usuarios:
# La lista es útil cuando necesitas una colección ordenada y modificable de elementos.
usuarios = ['Andrés', 'Katherin', 'Juan', 'Ana', 'Andrés', 'Camila']

# Mostrar la lista de usuarios
print("Lista de usuarios:", usuarios)  # 📝 Las listas permiten elementos duplicados y ordenados

# 2. TUPLAS para detalles de usuario:
# Una tupla es una estructura inmutable, ideal para almacenar datos que no deberían cambiar.
detalles_usuario = ('Andrés', 36, 'Ingeniero de sistemas')

# Mostrar los detalles del usuario
print("\nDetalles del usuario (tupla):", detalles_usuario)
# 📝 No se puede modificar una tupla, lo que garantiza la integridad de los datos.

# 3. CONJUNTO para eliminar duplicados:
# Los conjuntos no permiten elementos duplicados y son útiles para ver cuántos usuarios únicos hay.
usuarios_unicos = set(usuarios)

# Mostrar el conjunto de usuarios únicos
print("\nConjunto de usuarios únicos:", usuarios_unicos)
# 📝 Esto es útil para eliminar duplicados y realizar operaciones como uniones e intersecciones.

# 4. DICCIONARIO para mapear usuarios con roles:
# Los diccionarios permiten almacenar datos de manera clave-valor. En este caso, cada usuario tendrá un rol.
roles_usuarios = {
    'Andrés': 'Administrador',
    'Katherin': 'Psicóloga',
    'Juan': 'Desarrollador',
    'Ana': 'Diseñadora',
    'Camila': 'Project Manager'
}

# Mostrar el diccionario con roles
print("\nDiccionario de usuarios con roles:")
for usuario, rol in roles_usuarios.items():
    print(f"{usuario}: {rol}")
# 📝 Los diccionarios permiten un acceso rápido a los valores mediante sus claves y no admiten claves duplicadas.

# 5. FROZENSET para proteger un grupo de usuarios importantes:
# Un `frozenset` es un conjunto inmutable, útil cuando quieres asegurar que un grupo de elementos no pueda ser modificado.
usuarios_importantes = frozenset(['Andrés', 'Camila'])

# Mostrar el frozenset
print("\nUsuarios importantes (frozenset):", usuarios_importantes)
# 📝 Un `frozenset` no permite la modificación de su contenido, lo que ayuda a proteger datos sensibles.

# Ejemplo de uso práctico:
# Verificar si un usuario está en la lista de importantes
usuario_a_verificar = 'Camila'
if usuario_a_verificar in usuarios_importantes:
    print(f"\n{usuario_a_verificar} es un usuario importante y no puede ser modificado.")
else:
    print(f"\n{usuario_a_verificar} no está en la lista de usuarios importantes.")
