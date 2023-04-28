from TablaHashEspecial.tda_tabla_hash import *
from TablaHashEspecial.tda_lista import *
from FuncionesEspeciales.funciones_especiales import *
import random

tablaLegiones = crear_tabla(6)
tablaNumeros = crear_tabla(10)

legiones = ["TK", "CT", "TF", "FO", "FN", "FL"]

# Vamos a generar 2000 stormtroopers, los cuales se les escogerá una legion aleatoriamente, y un numero de 4 digitos aleatorio

numeros = []

for i in range(1999):
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
    
stormtrooper = {
    "legion": "FN",
    "numero": "2187",
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
        numero = input("Ingrese el número de stormtrooper que desea eliminar: ")
        posicion_legion = funcion_hash_legion(legion)
        posicion_numero = funcion_hash_numeros(numero, len(tablaNumeros))
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
                mision = input("Ingrese la misión que desea asignar: ")
                asignar_mision_legion(tablaLegiones, legion, mision)
            else:
                print("Opción incorrecta")
            submenu_respuesta = submenu()
    elif respuesta == 4:
        submenu_respuesta = submenu()
        while submenu_respuesta != 0:
            if submenu_respuesta == 1:
                numero = input("Ingrese los tres últimos dígitos de Stormtroopers que desea buscar: ")
                filtrar_numeros(tablaNumeros, numero)
            elif submenu_respuesta == 2:
                numero = input("Ingrese los tres últimos dígitos de Stormtroopers que desea asignarles la misión: ")
                mision = input("Ingrese la misión que desea asignar: ")
                asignar_mision_numeros(tablaNumeros, numero, mision)
            else:
                print("Opción incorrecta")
            submenu_respuesta = submenu()
    else:
        print("Opción incorrecta")
    respuesta = menu()
print("Gracias por utilizar el programa")



