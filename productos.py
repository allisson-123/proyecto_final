def registrar_producto(nombres, precios, stock):
    print("\n=== REGISTRAR PRODUCTO ===")
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacio.")
        return nombres, precios, stock
    nombre = nombre.lower()
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad disponible: "))
    if precio <= 0 or cantidad < 0:
        print("El precio debe ser mayor que cero y la cantidad no puede ser negativa.")
    else:
        nombres = nombres + [nombre]
        precios = precios + [precio]
        stock = stock + [cantidad]
        print("Producto registrado correctamente.")
    return nombres, precios, stock

def mostrar_productos(nombres, precios, stock):
    print("\n=== LISTA DE PRODUCTOS ===")

    if len(nombres) == 0:
        print("No hay productos registrados.")
    else:
        for i in range(len(nombres)):
            print(
                i + 1, "-", nombres[i],
                "| Precio: S/", precios[i],
                "| Stock:", stock[i]
                )

def buscar_producto(nombres, precios, stock):
    print("\n=== BUSCAR PRODUCTO ===")

    buscar = input("Ingrese el nombre del producto: ").strip().lower()
    encontrado = False

    for i in range(len(nombres)):
        if buscar in nombres[i]:
            print("Nombre:", nombres[i])
            print("Precio: S/", precios[i])
            print("Stock:", stock[i])
            encontrado = True

    if encontrado == False:
        print("No se encontro el producto.")
