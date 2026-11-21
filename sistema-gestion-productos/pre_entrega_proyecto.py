# Acá se guardarán todos los productos.
# Cada producto será una sublista: [nombre, categoría, precio]
productos = []

# Pide los datos y agrega un producto a la lista.
def agregar_producto():
    nombre = input("Ingresá el nombre del producto: ").strip()

    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Ingresá el nombre del producto: ").strip()

    categoria = input("Ingresá la categoría del producto: ").strip()

    while categoria == "":
        print("La categoría no puede estar vacía.")
        categoria = input("Ingresá la categoría del producto: ").strip()

    precio_texto = input("Ingresá el precio, sin centavos: ").strip()

    # Se comprueba que el precio tenga solo dígitos.
    while not precio_texto.isdigit():
        print("El precio debe ser un número entero, sin centavos.")
        precio_texto = input("Ingresá el precio, sin centavos: ").strip()

    # Se convierte el texto ingresado a un número entero.
    precio = int(precio_texto)

    # Se guarda el producto como una sublista de tres elementos.
    productos.append([nombre, categoria, precio])

    print("Producto agregado correctamente.")


# Muestra todos los productos registrados.
def visualizar_productos():
    if len(productos) == 0:
        print("\nTodavía no hay productos registrados.")
    else:
        print("\n--- Productos registrados ---")

        # enumerate permite obtener el número y el producto.
        # start=1 hace que la numeración comience en 1.
        for numero, producto in enumerate(productos, start=1):
            print(
                f"{numero}. Nombre: {producto[0]} | "
                f"Categoría: {producto[1]} | "
                f"Precio: ${producto[2]}"
            )



# Busca productos cuyo nombre coincida con el texto ingresado.
def buscar_producto():
    nombre_buscado = input("Ingresá el nombre que querés buscar: ").strip()

    while nombre_buscado == "":
        print("La búsqueda no puede estar vacía.")
        nombre_buscado = input("Ingresá el nombre que querés buscar: ").strip()

    encontrados = 0

    print("\n--- Resultados de la búsqueda ---")

    for numero, producto in enumerate(productos, start=1):
        # lower() permite comparar sin distinguir mayúsculas de minúsculas.
        if nombre_buscado.lower() in producto[0].lower():
            print(
                f"{numero}. Nombre: {producto[0]} | "
                f"Categoría: {producto[1]} | "
                f"Precio: ${producto[2]}"
            )
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron productos con ese nombre.")


# Elimina un producto usando el número que aparece en la visualización.
def eliminar_producto():
    if len(productos) == 0:
        print("\nNo hay productos para eliminar.")
        return

    visualizar_productos()

    numero_texto = input(
        "\nIngresá el número del producto que querés eliminar: "
    ).strip()

    while (not numero_texto.isdigit() or
           int(numero_texto) < 1 or
           int(numero_texto) > len(productos)): 
        print("Ingresá un número válido.")
        numero_texto = input(
            "Ingresá el número del producto que querés eliminar: "
        ).strip()

    numero = int(numero_texto)
    # producto_eliminado = productos.pop(numero - 1)

   # La persona cuenta desde 1, pero los índices de la lista empiezan en 0.
    if numero >= 1 and numero <= len(productos):
        producto_eliminado = productos.pop(numero - 1)
        print(f"Se eliminó el producto: {producto_eliminado[0]}")
    else:
       print("Ese número no corresponde a ningún producto.")


# Menú principal. Se repite hasta elegir la opción 5.
while True:
    print("\n=== MENÚ DE PRODUCTOS ===")
    print("1. Agregar producto")
    print("2. Visualizar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        visualizar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("Programa finalizado.")
        break
    else:
        print("Opción incorrecta. Elegí un número del 1 al 5.")