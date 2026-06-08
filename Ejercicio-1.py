especialista_senior = 0
residentes_junior = 0

while True:
    try:
        cantidad_medicos = int(input("Bienvenido al hospital, por favor ingrese la cantidad de medicos que desea registrar: "))
        if cantidad_medicos <= 0:
            print ("¡Registro médico inválido! Ingresa un entero positivo para continuar")
        else:
            print("se han agregado", cantidad_medicos, "medicos")
            break
    except ValueError:
        print ("Registro medico inválido! Ingresa un entero positivo para continuar")

for i in range(cantidad_medicos):
    print("Ingresando al medico", (i+1))

    while True:
        nombre = input("Ingrese el nombre del profesional ( min. 6 caracteres, sin espacios): ").strip()
        if len(nombre) >=6 and " " not in nombre:
            print ("Nombre profesional valido")
            break
        else:
            print("Nombre profesional incorrecto, su nombre debe tener al menos 6 letras y no tener espacios")

    while True:
        try:
            experiencia_clinica = int(input("Por favor, ingresa los años de experiencia del medico: "))
            if experiencia_clinica <= 0:
                print("Error clinico, ingresa un numero entero positivo para la experiencia.")
            else:
                break
        except ValueError:
            print("Error clinico, ingresa un numero entero positivo para la experiencia.")

    if experiencia_clinica > 5:
        especialista_senior += 1
    elif experiencia_clinica <= 5:
        residentes_junior += 1

print("El hospital cuenta con", especialista_senior, "Especialistas Senior y", residentes_junior, "Residentes Junior! Sistema listo para operar!")
