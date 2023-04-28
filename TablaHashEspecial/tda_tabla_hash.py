from TablaHashEspecial.tda_lista import *

# Esta funcion de crear nos sirve tanto para Legion como para Numeros
def crear_tabla(tamano):
    tabla = [None]*tamano
    return tabla

# Esta funcion de cantidad nos sirve tanto para Legion como para Numeros
def cantidad_elementos(tabla):
    return len(tabla)-tabla.count(None)

# Esta funcion de cantidad total nos sirve tanto para Legion como para Numeros
def cantidad_elementos_totales(tabla):
    return sum(tamano(lista) for lista in tabla if lista is not None)

# Esta funcion nos permite visualizar todos los stormtroopers que existen en la tabla hash de Legion
def barrido_total(tabla):
    for lista in tabla:
        if lista is not None:
            barrido(lista)

#------------------------------------------------------------------------------------------

# Se crearon funciones necesarias para poder agregar y buscar en la tabla hash de Legion
def funcion_hash_legion(dato, tamano_tabla):
    valor_ascii = sum(ord(caracter) for caracter in dato)
    valor_hash = valor_ascii % tamano_tabla
    # Gracias a que hay colision de hashes, utilizamos el metodo de la division entre 3 para poder evitarlas.
    if dato == "TK":
        valor_hash = (valor_hash + tamano_tabla // 3) % tamano_tabla
    elif dato == "CT":
        valor_hash = (valor_hash + 2 * tamano_tabla // 3) % tamano_tabla
    elif dato == "TF":
        valor_hash = (valor_hash + tamano_tabla // 4) % tamano_tabla
    elif dato == "FO":
        valor_hash = (valor_hash + 3 * tamano_tabla // 4) % tamano_tabla
    return valor_hash

def agregar_legion(tabla, dato):
    posicion = funcion_hash_legion(dato["legion"], len(tabla))
    if(tabla[posicion] is None):
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato)

def filtrar_legion(tabla, buscado):
    posicion = funcion_hash_legion(buscado, len(tabla))
    if(tabla[posicion] is not None):
        barrido(tabla[posicion])
    else:
        print("No existe la legion", buscado, "en la tabla hash.")


def buscar_tabla_legion(tabla, buscado):
    pos = None
    posicion = funcion_hash_legion(buscado, len(tabla))
    print(tabla[posicion])
    if(tabla[posicion] is not None):
        pos = buscar(tabla[posicion], buscado)
    return pos

def asignar_mision_legion(tabla, buscado, mision):
    posicion = funcion_hash_legion(buscado, len(tabla))
    if(tabla[posicion] is not None):
        asignar_mision(tabla[posicion], mision)
    else:
        print("No existe la legion", buscado, "en la tabla hash.")
# ----------------------------------------------------------------------------------------------

# Se crearon funciones necesarias para poder agregar y buscar en la tabla hash de Numeros
def funcion_hash_numeros(dato, tamano_tabla):
    dato = int(dato)
    if dato == 0:
        return 0
    return dato % tamano_tabla

def agregar_numeros(tabla, dato):
    posicion = funcion_hash_numeros(dato["numero"][0], len(tabla))
    print(posicion)
    if(tabla[posicion] is None):
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato)

def filtrar_numeros(tabla, buscado):
    for lista in tabla:
        if lista is not None:
            barrido_numero(lista, buscado)

def buscar_tabla_numeros(tabla, buscado):
    pos = None
    posicion = funcion_hash_numeros(buscado, len(tabla))
    print(tabla[posicion])
    if(tabla[posicion] is not None):
        pos = buscar(tabla[posicion], buscado)
    return pos

def asignar_mision_numeros(tabla, buscado, mision):
    for lista in tabla:
        if lista is not None:
            asignar_mision_numero(lista, buscado, mision)
# ----------------------------------------------------------------------------------------------
