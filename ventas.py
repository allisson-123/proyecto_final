from datetime import datetime

def registrar_venta(nombres, precios, stock):
    print("\n=== REGISTRAR VENTA ===")

    if len(nombres) == 0:
        print("No hay productos registrados.")
        return 0

    total = 0
    productos_vendidos = []
    cantidades = []
    precios_venta = []
    subtotales = []

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

                productos_vendidos = productos_vendidos + [nombres[posicion]]
                cantidades = cantidades + [cantidad]
                precios_venta = precios_venta + [precios[posicion]]
                subtotales = subtotales + [subtotal]

                print("Producto vendido correctamente.")
                print("Subtotal: S/", subtotal)

    if total > 0:
        fecha = datetime.now().strftime("%d/%m/%Y")
        hora = datetime.now().strftime("%H:%M:%S")

        print("\n================================")
        print("       MINIMARKET TOKE")
        print("      COMPROBANTE DE VENTA")
        print("================================")
        print("Fecha:", fecha)
        print("Hora:", hora)
        print("--------------------------------")

        for i in range(len(productos_vendidos)):
            print("Producto:", productos_vendidos[i])
            print("Cantidad:", cantidades[i])
            print("Precio: S/", format(precios_venta[i], ".2f"))
            print("Subtotal: S/", format(subtotales[i], ".2f"))
            print("--------------------------------")

        print("TOTAL: S/", format(total, ".2f"))
        print("================================")
        print("      Gracias por su compra")
        print("================================")

        archivo = open("comprobantes.txt", "a")
        archivo.write("================================\n")
        archivo.write("       MINIMARKET TOKE\n")
        archivo.write("      COMPROBANTE DE VENTA\n")
        archivo.write("================================\n")
        archivo.write("Fecha: " + fecha + "\n")
        archivo.write("Hora: " + hora + "\n")
        archivo.write("--------------------------------\n")

        for i in range(len(productos_vendidos)):
            archivo.write("Producto: " + productos_vendidos[i] + "\n")
            archivo.write("Cantidad: " + str(cantidades[i]) + "\n")
            archivo.write("Precio: S/ " + format(precios_venta[i], ".2f") + "\n")
            archivo.write("Subtotal: S/ " + format(subtotales[i], ".2f") + "\n")
            archivo.write("--------------------------------\n")

        archivo.write("TOTAL: S/ " + format(total, ".2f") + "\n")
        archivo.write("================================\n\n")
        archivo.close()

        print("Comprobante guardado en comprobantes.txt")
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