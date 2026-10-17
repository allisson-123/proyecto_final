from productos import registrar_producto, mostrar_productos, buscar_producto

nombres = []
precios = []
stock = []

print("================================")
print("      MINIMARKET TOKE")
print("================================")

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Ordenar productos")
    print("5. Actualizar stock")
    print("6. Registrar venta")
    print("7. Ver registro de ventas")
    print("8. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombres, precios, stock = registrar_producto(nombres, precios, stock)

    elif opcion == "2":
        mostrar_productos(nombres, precios, stock)

    elif opcion == "3":
        buscar_producto(nombres, precios, stock)

    elif opcion == "4":
        print("Esta opcion se implementara en el commit 3.")

    elif opcion == "5":
        print("Esta opcion se implementara en el commit 3.")

    elif opcion == "6":
        print("Esta opcion se implementara en el commit 4.")

    elif opcion == "7":
        print("Esta opcion se implementara en el commit 5.")

    elif opcion == "8":
        print("Gracias por usar el sistema TOKE.")
        break

    else:
        print("Opcion incorrecta.")
