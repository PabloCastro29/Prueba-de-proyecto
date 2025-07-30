items_list = []

while True:
    print("\n1. Agregar")
    print("2. Buscar")
    print("3. Eliminar")
    print("4. Mostrar todo")
    print("5. Salir")
    list_option = input("Elija opción: ")

    if list_option == "1":
        item = input("Elemento a agregar: ")
        items_list.append(item)
    elif list_option == "2":
        item = input("Elemento a buscar: ")
        if item in items_list:
            print(item, "está en la lista.")
        else:
            print(item, "no encontrado.")
    elif list_option == "3":
        item = input("Elemento a eliminar: ")
        if item in items_list:
            items_list.remove(item)
            print(item, "eliminado.")
        else:
            print(item, "no encontrado.")
    elif list_option == "4":
        print("Lista:", items_list)
    elif list_option == "5":
        break
    else:
        print("Opción no válida.")
