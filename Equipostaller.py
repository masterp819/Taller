from Clientes import Cliente
from Equipos import Equipo

clientes = []

def ingresar_cliente():
    apellidos = input("Apellidos: ")
    nombres = input("Nombres: ")
    telefono = input("Teléfono: ")
    cliente = Cliente(apellidos, nombres, telefono)
    clientes.append(cliente)
    print("Cliente agregado exitosamente.\n")

def ver_clientes():
    if not clientes:
        print("No hay clientes registrados.\n")
        return
    for idx, cliente in enumerate(clientes):
        print(f"{idx+1}. {cliente}")
    print()

def agregar_equipo():
    if not clientes:
        print("Primero debe ingresar clientes.\n")
        return
    ver_clientes()
    idx = int(input("Seleccione el número de cliente: ")) - 1
    if 0 <= idx < len(clientes):
        numero_parte = input("Número de Parte: ")
        tipo_equipo = input("Tipo de Equipo: ")
        descripcion = input("Descripción del problema: ")
        equipo = Equipo(numero_parte, tipo_equipo, descripcion)
        clientes[idx].agregar_equipo(equipo)
        print("Equipo agregado exitosamente.\n")
    else:
        print("Cliente no válido.\n")

def ver_equipos_por_cliente():
    if not clientes:
        print("No hay clientes registrados.\n")
        return
    ver_clientes()
    idx = int(input("Seleccione el número de cliente: ")) - 1
    if 0 <= idx < len(clientes):
        cliente = clientes[idx]
        if not cliente.equipos:
            print("Este cliente no tiene equipos registrados.\n")
        else:
            print(f"Equipos de {cliente.nombres} {cliente.apellidos}:")
            for equipo in cliente.equipos:
                print(f"- {equipo}")
            print()
    else:
        print("Cliente no válido.\n")

def menu():
    while True:
        print("=== Menú Taller de Reparación ===")
        print("1. Ingresar Cliente")
        print("2. Ver Clientes")
        print("3. Agregar Equipo")
        print("4. Ver Equipos por Cliente")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ingresar_cliente()
        elif opcion == "2":
            ver_clientes()
        elif opcion == "3":
            agregar_equipo()
        elif opcion == "4":
            ver_equipos_por_cliente()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.\n")

if __name__ == "__main__":
    menu()