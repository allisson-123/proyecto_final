from productos import (
    registrar_producto,
    mostrar_productos,
    buscar_producto,
    ordenar_productos,
    actualizar_stock,
    guardar_productos,
    cargar_productos
    )

from ventas import (
    registrar_venta,
    guardar_venta,
    cargar_ventas,
    mostrar_registro
)

nombres, precios, stock = cargar_productos()
registro_ventas = cargar_ventas()

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
        guardar_productos(nombres, precios, stock)

    elif opcion == "2":
        mostrar_productos(nombres, precios, stock)

    elif opcion == "3":
        buscar_producto(nombres, precios, stock)

    elif opcion == "4":
        nombres, precios, stock = ordenar_productos(nombres, precios, stock)
        guardar_productos(nombres, precios, stock)

    elif opcion == "5":
        actualizar_stock(nombres, precios, stock)
        guardar_productos(nombres, precios, stock)

    elif opcion == "6":
        total = registrar_venta(nombres, precios, stock)

        if total > 0:
            registro_ventas = registro_ventas + [total]
            guardar_venta(total)
            guardar_productos(nombres, precios, stock)

    elif opcion == "7":
        mostrar_registro(registro_ventas)

    elif opcion == "8":
        print("Gracias por usar el sistema TOKE.")
        guardar_productos(nombres, precios, stock)
        break

    else:
        print("Opcion incorrecta.")
