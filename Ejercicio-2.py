Libros_Disponibles = 120
Libros_Recerbados = 0 

print("Bienvenido a la biblioteca, por favor seleccione una opcion del menu para continuar")

while True:
    print("===MENU PRINCIPAL===")
    print("1. Libros disponibles")
    print("2. Realizar prestamo")
    print("3. Devolucion prestamo")
    print("4. Historial de pretamos")
    print("5. Salir")
    
    while True:
        try:
            opcion = int(input("ingrese una opcion: "))
            break
        except ValueError:
            print("¡Debe ingresar una opcion valida!")
    
    if opcion == 1:
        print("la cantidad de libros disponibles es: ", Libros_Disponibles)

    elif opcion == 2:
        while True:
            try:
                cantidad_a_reservar = int(input("ingrese la cantidad de libros a reservar: "))
                if cantidad_a_reservar <= 0:
                    print("La cantidad debe ser un numero positivo")
                elif cantidad_a_reservar <= Libros_Disponibles:
                    print("reservando", cantidad_a_reservar, "libros")
                    Libros_Disponibles -= cantidad_a_reservar
                    Libros_Recerbados += cantidad_a_reservar
                    break 
            except ValueError:
                print("¡Debe ingresar una opcion valida!")

    elif opcion == 3:
        while True:
            try:
                devolver_libros = int(input("Ingrese la cantidad de libros a devolver: "))
                if devolver_libros <= 0:
                    print("La cantidad debe ser un numero positivo")

                elif devolver_libros > Libros_Recerbados:
                    print("No puede devolver mas libros de los que estan prestados")
                    
                else:  
                    print("Devolviendo", devolver_libros, "libros")
                    Libros_Disponibles += devolver_libros
                    Libros_Recerbados -= devolver_libros
                    break
            except ValueError:
                print("Debe ingresar una cantidad valida.")
                

    elif opcion == 4:
        print("El total de prestamos activos actualmente es: ", Libros_Recerbados)
        print("La cantidad de libros disponibles es: ", Libros_Disponibles)
    elif opcion == 5:
        print("¡Gracias por usar el sistema, hasta pronto!")
        break
    else:
        print("Opcion no valida. Por favor vuelva a intentarlo.")