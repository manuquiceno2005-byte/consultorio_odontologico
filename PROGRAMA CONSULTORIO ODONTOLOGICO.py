# Consultorio odontologico
# Heliana Manuela Quiceno Marin

clientes = []


def leer_entero_positivo(mensaje):
    """Pide un número entero mayor que cero hasta que sea válido."""
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            print("Error: La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")


def registrar_cliente():
    print("\n--- INGRESO DE DATOS DEL CLIENTE ---")
    cedula = input("Ingrese la cedula: ")
    nombre = input("Ingrese el nombre completo: ")
    telefono = input("Ingrese el telefono: ")

    # Tipo de cliente (se repite hasta que sea válido)
    print("\nTipos de Cliente:")
    print("1 Particular")
    print("2 EPS")
    print("3 Prepagada")

    tipo_cliente = ""
    valor_cita = 0
    while tipo_cliente == "":
        opcion_cliente = input("Seleccione una opción (1 - 3): ")
        if opcion_cliente == "1":
            tipo_cliente = "Particular"
            valor_cita = 80000
        elif opcion_cliente == "2":
            tipo_cliente = "EPS"
            valor_cita = 5000
        elif opcion_cliente == "3":
            tipo_cliente = "Prepagada"
            valor_cita = 30000
        else:
            print("Opción de cliente no válida, intente de nuevo.")

    # Tipo de atención (se repite hasta que sea válida)
    print("\nTipos de atencion:")
    print("1 Limpieza")
    print("2 Calzas")
    print("3 Extraccion")
    print("4 Diagnostico")

    tipo_atencion = ""
    valor_atencion_unitario = 0
    while tipo_atencion == "":
        opcion_atencion = input("Seleccione una opcion (1-4): ")

        if opcion_atencion == "1":
            tipo_atencion = "Limpieza"
            if tipo_cliente == "Particular":
                valor_atencion_unitario = 60000
            else:
                valor_atencion_unitario = 0

        elif opcion_atencion == "2":
            tipo_atencion = "Calzas"
            if tipo_cliente == "Particular":
                valor_atencion_unitario = 80000
            elif tipo_cliente == "EPS":
                valor_atencion_unitario = 40000
            else:  # Prepagada
                valor_atencion_unitario = 10000

        elif opcion_atencion == "3":
            tipo_atencion = "Extraccion"
            if tipo_cliente == "Particular":
                valor_atencion_unitario = 100000
            elif tipo_cliente == "EPS":
                valor_atencion_unitario = 40000
            else:  # Prepagada
                valor_atencion_unitario = 10000

        elif opcion_atencion == "4":
            tipo_atencion = "Diagnostico"
            if tipo_cliente == "Particular":
                valor_atencion_unitario = 50000
            else:
                valor_atencion_unitario = 0

        else:
            print("Opción de atención no válida, intente de nuevo.")

    # Regla del taller: Limpieza y Diagnostico siempre cantidad 1
    if tipo_atencion == "Limpieza" or tipo_atencion == "Diagnostico":
        cantidad = 1
        print("Para Limpieza y Diagnostico la cantidad es 1.")
    else:
        cantidad = leer_entero_positivo(f"Ingrese la cantidad para {tipo_atencion} (mayor a 0): ")

    # Prioridad (validada)
    prioridad = ""
    while prioridad not in ("Normal", "Urgente"):
        prioridad = input("Prioridad de atencion (Normal/Urgente): ").strip().capitalize()
        if prioridad not in ("Normal", "Urgente"):
            print("Escriba Normal o Urgente.")

    fecha = input("Fecha de la cita (dd/mm/aaaa): ")

    # Cálculo del valor total
    costo_atencion_total = valor_atencion_unitario * cantidad
    total_pagar = valor_cita + costo_atencion_total

    # Guardar el cliente en la lista
    nuevo_cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tipo_cliente": tipo_cliente,
        "tipo_atencion": tipo_atencion,
        "cantidad": cantidad,
        "prioridad": prioridad,
        "fecha": fecha,
        "valor_cita": valor_cita,
        "costo_atencion": costo_atencion_total,
        "total_pagar": total_pagar,
    }

    clientes.append(nuevo_cliente)
    print("\n>>> Cliente registrado! Total a pagar: $", total_pagar)


def calcular_estadisticas():
    if len(clientes) == 0:
        print("\nNo hay clientes registrados en el sistema.")
        return

    total_clientes = len(clientes)
    ingresos_totales = 0
    clientes_extraccion = 0

    for c in clientes:
        ingresos_totales += c["total_pagar"]
        if c["tipo_atencion"] == "Extraccion":
            clientes_extraccion += 1

    print("\n-------------------------------------")
    print("        ESTADISTICAS GENERALES")
    print("-------------------------------------")
    print("1 Total de clientes:", total_clientes)
    print("2 Ingresos totales recibidos: $", ingresos_totales)
    print("3 Clientes para extraccion de dientes:", clientes_extraccion)
    print("-------------------------------------")


def ordenar_y_buscar():
    if len(clientes) == 0:
        print("\nNo hay clientes registrados.")
        return

    # Ordenamiento burbuja - mayor a menor por costo de atención
    n = len(clientes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if clientes[j]["costo_atencion"] < clientes[j + 1]["costo_atencion"]:
                # intercambiar
                clientes[j], clientes[j + 1] = clientes[j + 1], clientes[j]

    print("\n--- LISTA ORDENADA POR VALOR DE ATENCION (MAYOR A MENOR) ---")
    for c in clientes:
        print(f"Nombre: {c['nombre']} | Cedula: {c['cedula']} | "
              f"Servicio: {c['tipo_atencion']} | "
              f"Costo atencion: ${c['costo_atencion']} | "
              f"Total pagar: ${c['total_pagar']}")

    # Búsqueda por cédula
    print("\n--- BUSQUEDA DE CLIENTE ---")
    cedula_buscar = input("Ingrese la cedula a buscar: ")
    encontrado = False

    for c in clientes:
        if c["cedula"] == cedula_buscar:
            print("\nCliente Encontrado:")
            print("Cedula:", c["cedula"])
            print("Nombre:", c["nombre"])
            print("Telefono:", c["telefono"])
            print("Tipo cliente:", c["tipo_cliente"])
            print("Atencion:", c["tipo_atencion"], "(Cantidad:", c["cantidad"], ")")
            print("Prioridad:", c["prioridad"])
            print("Fecha:", c["fecha"])
            print("Valor cita: $", c["valor_cita"])
            print("Costo atencion: $", c["costo_atencion"])
            print("Total a pagar: $", c["total_pagar"])
            encontrado = True
            break

    if not encontrado:
        print("No se encontro ningun cliente con la cedula ingresada")


# Menú principal
opcion = ""
while opcion != "4":
    print("\n===== MENU CONSULTORIO =====")
    print("1 Registrar cliente")
    print("2 Ver estadisticas")
    print("3 Ordenar clientes y buscar por cedula")
    print("4 Salir")
    opcion = input("Elija una opcion: ")

    if opcion == "1":
        registrar_cliente()
    elif opcion == "2":
        calcular_estadisticas()
    elif opcion == "3":
        ordenar_y_buscar()
    elif opcion == "4":
        print("Saliendo del programa...")
    else:
        print("Opcion no valida, intente nuevamente")
   
        
     
        






