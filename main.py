from TablaHashEspecial.tda_tabla_hash import *
from TablaHashEspecial.tda_lista import *
from FuncionesEspeciales.funciones_especiales import *

import random

tablaLegiones = crear_tabla(6)
tablaNumeros = crear_tabla(10)

legiones = ["TK", "CT", "TF", "FO", "FN", "FL"]

# Vamos a generar 2000 stormtroopers, los cuales se les escogerá una legion aleatoriamente, y un numero de 4 digitos aleatorio

numeros = []

for i in range(2000):
    numero = generar_num_storm()
    while numero in numeros:
        numero = generar_num_storm()
    numeros.append(numero)
    legion = random.choice(legiones)
    stormtrooper = {
        "legion": legion,
        "numero": numero,
        "misiones": []
    }
    agregar_legion(tablaLegiones, stormtrooper)
    agregar_numeros(tablaNumeros, stormtrooper)


# Menu principal
respuesta = menu()
while respuesta != 0:
    if respuesta == 1:
        barrido_total(tablaLegiones)
    elif respuesta == 2:
        legion = input("Ingrese la legión del stormtrooper que desea eliminar: ")
        numero = int(input("Ingrese el número de stormtrooper que desea eliminar: "))
        posicion_legion = buscar_tabla_legion(tablaLegiones, legion)
        posicion_numero = buscar_tabla_numeros(tablaNumeros, numero)
        if posicion_legion is not None:
            eliminar(tablaLegiones[posicion_legion], numero)
            print("Se ha eliminado el stormtrooper ", legion, "-", numero, " de la lista de legiones")
        else:
            print("No se ha encontrado ningun stormtrooper con identificador ", legion, "-", numero , " en la lista de legiones")
        
        if posicion_numero is not None:
            eliminar(tablaNumeros[posicion_numero], numero)
            print("Se ha eliminado el stormtrooper ", legion, "-", numero, " de la lista de dígitos")
        else:
            print("No se ha encontrado ningun stormtrooper con identificador ", legion, "-", numero, " en la lista de dígitos")
    elif respuesta == 3:
        submenu_respuesta = submenu()
        while submenu_respuesta != 0:
            if submenu_respuesta == 1:
                legion = input("Ingrese la legión que desea buscar: ")
                filtrar_legion(tablaLegiones, legion)
            elif submenu_respuesta == 2:
                legion = input("Ingrese la legión a la cual desea asignar la misión: ")
                posicion_legion = buscar_tabla_legion(tablaLegiones, legion)
                if posicion_legion is not None:
                    mision = input("Ingrese la misión que desea asignar: ")
                    asignar_mision_legion(tablaLegiones, legion, mision)
                else:
                    print("No se ha encontrado la legión ", legion, " en la tabla de legiones")
            else:
                print("Opción incorrecta")
            submenu_respuesta = submenu()
    elif respuesta == 4:
        submenu_respuesta = submenu()
        while submenu_respuesta != 0:
            if submenu_respuesta == 1:
                numero = int(input("Ingrese los tres últimos dígitos de Stormtroopers que desea buscar: "))
                filtrar_numeros(tablaNumeros, numero)
            elif submenu_respuesta == 2:
                numero = int(input("Ingrese el número al cual desea asignar la misión: "))
                posicion_numero = buscar_tabla_numeros(tablaNumeros, numero)
                if posicion_numero is not None:
                    mision = input("Ingrese la misión que desea asignar: ")
                    asignar_mision_numeros(tablaNumeros, numero, mision)
                else:
                    print("No se ha encontrado el número ", numero, " en la tabla de dígitos")
            else:
                print("Opción incorrecta")
            submenu_respuesta = submenu()
    else:
        print("Opción incorrecta")
    respuesta = menu()
print("Gracias por utilizar el programa")



