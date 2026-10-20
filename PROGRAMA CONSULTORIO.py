# CONSULTORIO ODONTOLOGICO

# Lista de pacientes registrados
pacientes = [
    {
        "nombre": "Manuela Quiceno",
        "procedimiento": "Extraccion dental",
        "prioridad": "Urgente",
        "fecha": "2026-10-12"
    },
    {
        "nombre": "Heliana Quiceno",
        "procedimiento": "Limpieza dental",
        "prioridad": "Normal",
        "fecha": "2026-10-13"
    },
    {
        "nombre": "Sofia",
        "procedimiento": "Extraccion dental",
        "prioridad": "Urgente",
        "fecha": "2026-10-14"
    },
    {
        "nombre": "Juan",
        "procedimiento": "Extraccion dental",
        "prioridad": "Normal",
        "fecha": "2026-10-15"
    },
    {
        "nombre": "Maria",
        "procedimiento": "Extraccion dental",
        "prioridad": "Urgente",
        "fecha": "2026-10-18"
    }
]


# FUNCION PARA CREAR LA PILA DE URGENCIAS
def crear_pila():
    pila = []

    # Buscar solamente extracciones urgentes
    for paciente in pacientes:
        if (paciente["procedimiento"] == "Extraccion dental"
                and paciente["prioridad"] == "Urgente"):
            pila.append(paciente)

    # Ordenar de la fecha mas lejana a la mas cercana
    # para que la fecha mas cercana quede en la parte de encima
    pila.sort(key=lambda paciente: paciente["fecha"],
              reverse=True)

    return pila


# FUNCION PARA MOSTRAR EL INFORME DE URGENCIAS
def mostrar_informe(pila):
    print("\n--- INFORME DE PACIENTES URGENTES ---")

    if len(pila) == 0:
        print("No hay pacientes urgentes pendientes.")
    else:
        for paciente in reversed(pila):
            print("Nombre:", paciente["nombre"])
            print("Procedimiento:", paciente["procedimiento"])
            print("Prioridad:", paciente["prioridad"])
            print("Fecha:", paciente["fecha"])
            print("---------------------------")


# FUNCION PARA ATENDER LA PILA
def atender_urgencias(pila):
    print("\n--- ATENCION DE URGENCIAS ---")

    while len(pila) > 0:
        paciente = pila.pop()

        print("Atendiendo a:", paciente["nombre"])
        print("Fecha de cita:", paciente["fecha"])

    print("No quedan pacientes urgentes en la pila.")


# FUNCION PARA CREAR lA ATENCION DE LA COLA
def crear_cola():
    cola = []

    print("\n--- AGENDA DIARIA ---")

    # Los pacientes se agregan en el orden de la agenda
    for paciente in pacientes:
        cola.append(paciente)

        print(paciente["nombre"], "-", paciente["fecha"])

    return cola


# FUNCION PARA ATENDER LA COLA
def atender_cola(cola):
    print("\n--- ATENCION DE LA AGENDA DIARIA ---")

    while len(cola) > 0:
        paciente = cola.pop(0)

        print("Atendiendo a:", paciente["nombre"])
        print("Procedimiento:", paciente["procedimiento"])
        print("---------------------------")

    print("Todos los pacientes de la agenda fueron atendidos.")


# MENU PRINCIPAL
def menu():
    pila_urgencias = crear_pila()
    cola_atencion = []

    while True:
        print("\nCONSULTORIO ODONTOLOGICO")
        print("1. Ver informe de urgencias")
        print("2. Atender pacientes urgentes")
        print("3. Generar agenda diaria")
        print("4. Atender pacientes de la agenda")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_informe(pila_urgencias)

        elif opcion == "2":
            atender_urgencias(pila_urgencias)

        elif opcion == "3":
            cola_atencion = crear_cola()

        elif opcion == "4":
            atender_cola(cola_atencion)

        elif opcion == "5":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opcion incorrecta. Intente nuevamente.")


menu()
