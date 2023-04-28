import random

def menu():
    """
    Muestra las opciones del menú y solicita al usuario que ingrese una opción.

    Returns:
    int: Opción elegida por el usuario.
    """
    print("=================================================")
    print("> [1] - Visualizar Stormtroopers.\n> [2] - Eliminar un Stormtrooper.\n> [3] - Buscar Stormtroopers por Legión.\n> [4] - Buscar Stromtroopers por dígitos.\n> [0] - Salir.")
    print("=================================================\n")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def submenu():
    """
    Muestra las opciones del submenú y solicita al usuario que ingrese una opción.

    Returns:
    int: Opción elegida por el usuario.
    """
    print("=================================================")
    print("> [1] - Visualizar los Stormtroopers.\n> [2] - Asignar Misión.")
    print("=================================================\n")
    opcion = int(input("Ingrese una opcion: "))
    return opcion

def generar_num_storm():
    """
    Genera un número aleatorio de 4 dígitos sin repetición.

    Returns:
    str: Número generado como una cadena de caracteres.
    """
    numeros = random.sample(range(10), 4)
    numero_aleatorio = "".join(str(d) for d in numeros)
    return numero_aleatorio
