import os
import json

# Archivo JSON para guardar y cargar datos
ARCHIVO_JSON = "inventario.json"

# Función para limpiar la consola
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

# Función para guardar los datos en un archivo JSON
def guardar_datos(ids, nombre, precio, cantidad, descripcion):
    with open(ARCHIVO_JSON, "w") as archivo:
        json.dump({"ids": ids, "nombre": nombre, "precio": precio, "cantidad": cantidad, "descripcion": descripcion}, archivo)

# Función para cargar los datos desde un archivo JSON
def cargar_datos():
    if os.path.exists(ARCHIVO_JSON):
        with open(ARCHIVO_JSON, "r") as archivo:
            return json.load(archivo)
    else:
        return {"ids": [], "nombre": [], "precio": [], "cantidad": [], "descripcion": []}

# Mostrar el inventario actual
def mostrar_inventario(ids, nombre, precio, cantidad, descripcion):
    limpiar_consola()
    print("\nInventario actual:")
    if not ids:
        print("El inventario está vacío.")
    else:
        for i in range(len(ids)):
            print(f"{ids[i]}. Nombre: {nombre[i]}, Precio: {precio[i]}, Cantidad: {cantidad[i]}, Descripción: {descripcion[i]}")
    input("\nPresione Enter para continuar...")

# Agregar un nuevo objeto al inventario
def agregar_objeto(ids, nombre, precio, cantidad, descripcion):
    limpiar_consola()
    nuevo_nombre = input("Ingrese el nombre del nuevo objeto: ").capitalize()
    nuevo_precio = int(input("Ingrese el precio del objeto (en pesos): "))
    nueva_cantidad = int(input("Ingrese la cantidad disponible del objeto: "))
    nueva_descripcion = input("Ingrese una descripción para el objeto: ").capitalize()
    
    nuevo_id = max(ids) + 1 if ids else 1  # Generar ID autoincremental
    ids.append(nuevo_id)
    nombre.append(nuevo_nombre)
    precio.append(nuevo_precio)
    cantidad.append(nueva_cantidad)
    descripcion.append(nueva_descripcion)
    guardar_datos(ids, nombre, precio, cantidad, descripcion)
    
    print(f"\nEl objeto '{nuevo_nombre}' ha sido agregado al inventario con ID {nuevo_id}.")
    input("Presione Enter para continuar...")

# Eliminar un objeto del inventario
def eliminar_objeto(ids, nombre, precio, cantidad, descripcion):
    limpiar_consola()
    mostrar_inventario(ids, nombre, precio, cantidad, descripcion)
    id_eliminar = int(input("\nIngrese el ID del objeto que desea eliminar: "))
    
    if id_eliminar in ids:
        indice = ids.index(id_eliminar)
        print(f"El objeto '{nombre[indice]}' será eliminado.")
        del ids[indice]
        del nombre[indice]
        del precio[indice]
        del cantidad[indice]
        del descripcion[indice]
        guardar_datos(ids, nombre, precio, cantidad, descripcion)
        print("\nEl objeto ha sido eliminado.")
    else:
        print("ID no encontrado.")
    input("Presione Enter para continuar...")

# Ordenar los objetos por un campo específico
def ordenar_inventario(ids, nombre, precio, cantidad, descripcion):
    limpiar_consola()
    print("Ordenar inventario:")
    print("1. Por ID")
    print("2. Por nombre")
    print("3. Por precio")
    print("4. Por cantidad")
    print("5. Por descripción")
    opcion_campo = input("Seleccione un campo para ordenar (1-5): ")
    print("\n1. Ascendente\n2. Descendente")
    opcion_orden = input("Seleccione el orden (1-Ascendente, 2-Descendente): ")
    
    if opcion_campo not in ['1', '2', '3', '4', '5'] or opcion_orden not in ['1', '2']:
        print("Opción inválida.")
        input("Presione Enter para continuar...")
        return
    
    campo_map = {
        '1': ids,
        '2': nombre,
        '3': precio,
        '4': cantidad,
        '5': descripcion
    }
    
    campo = campo_map[opcion_campo]
    ascendente = opcion_orden == '1'
    
    # Ordenar basado en el campo seleccionado
    datos = list(zip(ids, nombre, precio, cantidad, descripcion))
    datos.sort(key=lambda x: x[int(opcion_campo) - 1], reverse=not ascendente)
    
    # Desempaquetar los datos ordenados
    ids[:], nombre[:], precio[:], cantidad[:], descripcion[:] = zip(*datos)
    
    guardar_datos(ids, nombre, precio, cantidad, descripcion)
    print("\nInventario ordenado correctamente.")
    mostrar_inventario(ids, nombre, precio, cantidad, descripcion)

# Buscar un objeto
def buscar_objeto(ids, nombre, precio, cantidad, descripcion):
    limpiar_consola()
    print("Buscar objeto:")
    print("1. Por ID")
    print("2. Por nombre")
    print("3. Por precio")
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == '1':
        id_buscar = int(input("Ingrese el ID del objeto: "))
        if id_buscar in ids:
            indice = ids.index(id_buscar)
            print(f"\nObjeto encontrado: ID: {ids[indice]}, Nombre: {nombre[indice]}, Precio: {precio[indice]}, Cantidad: {cantidad[indice]}, Descripción: {descripcion[indice]}")
        else:
            print(f"\nEl objeto con ID {id_buscar} no se encuentra en el inventario.")
    elif opcion == '2':
        nombre_buscar = input("Ingrese el nombre del objeto: ").capitalize()
        if nombre_buscar in nombre:
            indice = nombre.index(nombre_buscar)
            print(f"\nObjeto encontrado: ID: {ids[indice]}, Nombre: {nombre[indice]}, Precio: {precio[indice]}, Cantidad: {cantidad[indice]}, Descripción: {descripcion[indice]}")
        else:
            print(f"\nEl objeto '{nombre_buscar}' no se encuentra en el inventario.")
    elif opcion == '3':
        precio_buscar = int(input("Ingrese el precio del objeto: "))
        encontrados = [i for i in range(len(precio)) if precio[i] == precio_buscar]
        if encontrados:
            print("\nObjetos encontrados:")
            for i in encontrados:
                print(f"ID: {ids[i]}, Nombre: {nombre[i]}, Precio: {precio[i]}, Cantidad: {cantidad[i]}, Descripción: {descripcion[i]}")
        else:
            print(f"\nNo se encontraron objetos con el precio {precio_buscar}.")
    else:
        print("Opción inválida.")
    input("Presione Enter para continuar...")

# Menú principal
def menu():
    datos = cargar_datos()
    ids = datos["ids"]
    nombre = datos["nombre"]
    precio = datos["precio"]
    cantidad = datos["cantidad"]
    descripcion = datos["descripcion"]
    
    while True:
        limpiar_consola()
        print("\nMenú del inventario:")
        print("1. Mostrar inventario")
        print("2. Agregar un nuevo objeto")
        print("3. Ordenar inventario")
        print("4. Buscar un objeto")
        print("5. Eliminar un objeto")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == '1':
            mostrar_inventario(ids, nombre, precio, cantidad, descripcion)
        elif opcion == '2':
            agregar_objeto(ids, nombre, precio, cantidad, descripcion)
        elif opcion == '3':
            ordenar_inventario(ids, nombre, precio, cantidad, descripcion)
        elif opcion == '4':
            buscar_objeto(ids, nombre, precio, cantidad, descripcion)
        elif opcion == '5':
            eliminar_objeto(ids, nombre, precio, cantidad, descripcion)
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutar el programa
menu()
