import random

def menu():
    print("=================================================")
    print("> [1] - Visualizar Stormtroopers.\n> [2] - Eliminar un Stormtrooper.\n> [3] - Buscar Stormtroopers por Legión.\n> [4] - Buscar Stromtroopers por dígitos.\n> [0] - Salir.")
    print("=================================================\n")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def submenu():
    print("=================================================")
    print("> [1] - Visualizar los Stormtroopers.\n> [2] - Asignar Misión.")
    print("=================================================\n")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def generar_num_storm():
    # Generar una lista de 4 números aleatorios sin repetición
    numeros = random.sample(range(10), 4)
    # Unir los números en un solo número de 4 dígitos
    numero_aleatorio = "".join(str(d) for d in numeros)
    return numero_aleatorio