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

def ordenar_productos(nombres, precios, stock):
    print("\n=== ORDENAR PRODUCTOS ===")
    if len(nombres) <= 1:
        print("No hay suficientes productos para ordenar.")
        return nombres, precios, stock
    for i in range(len(nombres) - 1):
        for j in range(len(nombres) - 1 - i):
            if nombres[j] > nombres[j + 1]:

                temporal = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = temporal

                temporal = precios[j]
                precios[j] = precios[j + 1]
                precios[j + 1] = temporal

                temporal = stock[j]
                stock[j] = stock[j + 1]
                stock[j + 1] = temporal

    print("Productos ordenados alfabeticamente.")
    mostrar_productos(nombres, precios, stock)

    return nombres, precios, stock

def actualizar_stock(nombres, precios, stock):
    print("\n=== ACTUALIZAR STOCK ===")
    if len(nombres) == 0:
        print("No hay productos registrados.")
        return
    
    mostrar_productos(nombres, precios, stock)
    opcion = int(input("Seleccione el numero del producto: "))
    if opcion < 1 or opcion > len(nombres):
        print("Opcion incorrecta.")
    else:
        posicion = opcion - 1
        cantidad = int(input("Ingrese las unidades que llegaron: "))
        if cantidad > 0:
            stock[posicion] = stock[posicion] + cantidad
            print("Stock actualizado correctamente.")
            print("Nuevo stock:", stock[posicion])
        else:
            print("La cantidad debe ser mayor que cero.")

def guardar_productos(nombres, precios, stock):
    archivo = open("productos.txt", "w")

    for i in range(len(nombres)):
        archivo.write(
            nombres[i] + ";" + str(precios[i]) + ";" +
            str(stock[i]) + "\n"
        )

    archivo.close()
    print("Productos guardados correctamente.")

def cargar_productos():
    nombres = []
    precios = []
    stock = []

    archivo = open("productos.txt", "a+")
    archivo.seek(0)

    for linea in archivo:
        datos = linea.strip().split(";")

        if len(datos) == 3:
            nombres = nombres + [datos[0]]
            precios = precios + [float(datos[1])]
            stock = stock + [int(datos[2])]

    archivo.close()

    return nombres, precios, stock