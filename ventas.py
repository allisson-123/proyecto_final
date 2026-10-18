def registrar_venta(nombres, precios, stock):
    print("\n=== REGISTRAR VENTA ===")
    if len(nombres) == 0:
        print("No hay productos registrados.")
        return 0

    total = 0

    while True:
        print("\n=== PRODUCTOS DISPONIBLES ===")

        for i in range(len(nombres)):
            print(
                i + 1, "-", nombres[i],
                "| Precio: S/", precios[i],
                "| Stock:", stock[i])

        print("0. Terminar venta")

        opcion = input("Seleccione un producto: ")

        if opcion == "0":
            break

        if opcion < "1" or opcion > str(len(nombres)):
            print("Opcion incorrecta.")
        else:
            posicion = int(opcion) - 1

            cantidad = int(input("Ingrese la cantidad: "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")

            elif cantidad > stock[posicion]:
                print("No hay suficiente stock.")

            else:
                subtotal = precios[posicion] * cantidad
                total = total + subtotal
                stock[posicion] = stock[posicion] - cantidad

                print("Producto vendido correctamente.")
                print("Subtotal: S/", subtotal)

    if total > 0:
        print("\nTotal de la venta: S/", total)
        print("Venta finalizada.")
    else:
        print("No se registraron productos en esta venta.")

    return total

def guardar_venta(total):
    archivo = open("registro.txt", "a")
    archivo.write(str(total) + "\n")
    archivo.close()

def cargar_ventas():
    registro_ventas = []

    archivo = open("registro.txt", "a+")
    archivo.seek(0)

    for linea in archivo:
        registro_ventas = registro_ventas + [float(linea.strip())]

    archivo.close()

    return registro_ventas

def mostrar_registro(registro_ventas):
    print("\n=== REGISTRO DE VENTAS ===")

    if len(registro_ventas) == 0:
        print("Todavia no hay ventas registradas.")
    else:
        total_dia = 0

        for i in range(len(registro_ventas)):
            print("Venta", i + 1, "- S/", registro_ventas[i])
            total_dia = total_dia + registro_ventas[i]

        print("--------------------")
        print("Total vendido: S/", total_dia)