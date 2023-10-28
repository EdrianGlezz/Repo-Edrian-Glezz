lista_de_compras = []

while True:
    accion = input("Qué desea hacer? (Agregar/Ver/Salir): ")
    
    if accion.lower() == "agregar":
        item = input("Ingrese el item a agregar: ")
        lista_de_compras.append(item)
    elif accion.lower() == "ver":
        print("Lista de compras:")
        for item in lista_de_compras:
            print("-", item)
    elif accion.lower() == "salir":
        break
    else:
        print("Acción no válida.")
