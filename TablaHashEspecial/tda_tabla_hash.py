from TablaHashEspecial.tda_lista import *

def crear_tabla(tamano):
    """
    Crea una tabla hash vacía con el tamaño especificado.
    
    Parameters:
    tamano (int): El tamaño de la tabla hash que se desea crear.
    
    Returns:
    list: Una tabla hash vacía con el tamaño especificado.
    """
    tabla = [None]*tamano
    return tabla


def cantidad_elementos(tabla):
    """
    Calcula la cantidad de elementos en una tabla hash.
    
    Parameters:
    tabla (list): La tabla hash de la que se quiere obtener la cantidad de elementos.
    
    Returns:
    int: La cantidad de elementos presentes en la tabla hash.
    """
    return len(tabla)-tabla.count(None)


def cantidad_elementos_totales(tabla):
    """
    Calcula la cantidad total de elementos en una tabla hash, teniendo en cuenta todas las listas que la componen.
    
    Parameters:
    tabla (list): La tabla hash de la que se quiere obtener la cantidad total de elementos.
    
    Returns:
    int: La cantidad total de elementos presentes en la tabla hash.
    """
    return sum(tamano(lista) for lista in tabla if lista is not None)


def barrido_total(tabla):
    """
    Realiza un barrido completo de una tabla hash, mostrando todos los elementos de cada lista que la compone.
    
    Parameters:
    tabla (list): La tabla hash que se quiere barrer.
    
    Returns:
    None
    """
    for lista in tabla:
        if lista is not None:
            barrido(lista)


def funcion_hash_legion(dato):
    """
    Realiza una función hash para la tabla de "Legion" que retorna un valor entero correspondiente a la posición de inserción de un elemento.
    
    Parameters:
    dato (str): Un string que representa la "Legion" a la que pertenece un elemento.
    
    Returns:
    int: La posición de inserción del elemento en la tabla hash de "Legion".
    """
    if dato == "TK":
        valor_hash = 0
    elif dato == "CT":
        valor_hash = 1
    elif dato == "TF":
        valor_hash = 2
    elif dato == "FO":
        valor_hash = 3
    elif dato == "FN":
        valor_hash = 4
    elif dato == "FL":
        valor_hash = 5 
    return valor_hash


def agregar_legion(tabla, dato):
    """
    Agrega un elemento a la tabla hash de "Legion".
    
    Parameters:
    tabla (list): La tabla hash de "Legion".
    dato (dict): Un diccionario con información del elemento a agregar. Debe contener una clave "legion" con el valor de la "Legion" a la que pertenece el elemento.
    
    Returns:
    None
    """
    posicion = funcion_hash_legion(dato["legion"])
    if(tabla[posicion] is None):
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato)

def filtrar_legion(tabla, buscado):
    """
    Función que busca y filtra una legion en la tabla hash.
    
    Argumentos:
    tabla -- La tabla hash en la que se realizará la búsqueda.
    buscado -- El nombre de la legion que se desea buscar.
    
    Retorna:
    No retorna ningún valor. Imprime en pantalla el resultado de la búsqueda.
    """
    posicion = funcion_hash_legion(buscado)
    if(tabla[posicion] is not None):
        barrido(tabla[posicion])
    else:
        print("No existe la legion", buscado, "en la tabla hash.")


def buscar_tabla_legion(tabla, buscado):
    """
    Función que busca una legion en la tabla hash y retorna su posición.
    
    Argumentos:
    tabla -- La tabla hash en la que se realizará la búsqueda.
    buscado -- El nombre de la legion que se desea buscar.
    
    Retorna:
    Retorna la posición de la legion buscada en la tabla hash, o None si no se encuentra.
    """
    pos = None
    posicion = funcion_hash_legion(buscado)
    if(tabla[posicion] is not None):
        pos = buscar(tabla[posicion], buscado)
    return pos


def asignar_mision_legion(tabla, buscado, mision):
    """
    Función que asigna una misión a una legion en la tabla hash.
    
    Argumentos:
    tabla -- La tabla hash en la que se realizará la búsqueda.
    buscado -- El nombre de la legion a la que se le asignará la misión.
    mision -- La misión que se asignará a la legion.
    
    Retorna:
    No retorna ningún valor. Imprime en pantalla el resultado de la operación.
    """
    posicion = funcion_hash_legion(buscado)
    if(tabla[posicion] is not None):
        asignar_mision(tabla[posicion], mision)
    else:
        print("No existe la legion", buscado, "en la tabla hash.")


def funcion_hash_numeros(dato, tamano_tabla):
    """
    Función que calcula el valor hash de un dato numérico para ser utilizado en la tabla hash.
    
    Argumentos:
    dato -- El dato numérico a ser hasheado.
    tamano_tabla -- El tamaño de la tabla hash.
    
    Retorna:
    Retorna el valor hash del dato numérico.
    """
    dato = int(dato)
    if dato == 0:
        return 0
    return dato % tamano_tabla


def agregar_numeros(tabla, dato):
    """
    Función que agrega un dato numérico a la tabla hash.
    
    Argumentos:
    tabla -- La tabla hash en la que se agregará el dato.
    dato -- El dato numérico a ser agregado.
    
    Retorna:
    No retorna ningún valor. Agrega el dato a la tabla hash.
    """
    posicion = funcion_hash_numeros(dato["numero"][0], len(tabla))
    if(tabla[posicion] is None):
        tabla[posicion] = Lista()
    insertar(tabla[posicion], dato)

def filtrar_numeros(tabla, buscado):
    """
    Busca en la tabla hash de números los registros que contengan el número buscado.
    Recorre todas las listas que hay en la tabla y en cada una de ellas busca el número.
    Si encuentra registros con el número buscado, los muestra en pantalla.
    
    Parameters:
    tabla (list): La tabla hash de números a filtrar.
    buscado (int): El número que se desea buscar en la tabla.
    
    Returns:
    None
    """
    for lista in tabla:
        if lista is not None:
            barrido_numero(lista, buscado)


def buscar_tabla_numeros(tabla, buscado):
    """
    Busca en la tabla hash de números el registro que contiene el número buscado.
    Utiliza la función de hash para calcular la posición donde debería estar el registro
    que contiene el número buscado. Luego, busca el registro en la lista correspondiente
    a esa posición.
    
    Parameters:
    tabla (list): La tabla hash de números en la que se va a buscar el número.
    buscado (int): El número que se desea buscar en la tabla.
    
    Returns:
    int or None: La posición del registro que contiene el número buscado, si lo encuentra.
    None, si no lo encuentra.
    """
    pos = None
    posicion = funcion_hash_numeros(buscado, len(tabla))
    if(tabla[posicion] is not None):
        pos = buscar(tabla[posicion], buscado)
    return pos

def asignar_mision_numeros(tabla, buscado, mision):
    """
    Asigna una misión a los registros de la tabla hash de números que contengan el número buscado.
    Recorre todas las listas que hay en la tabla y en cada una de ellas busca el número buscado.
    Si encuentra registros con el número buscado, les asigna la misión.
    
    Parameters:
    tabla (list): La tabla hash de números en la que se van a asignar misiones.
    buscado (int): El número que se desea buscar en la tabla para asignar la misión.
    mision (str): La misión que se va a asignar a los registros que contengan el número buscado.
    
    Returns:
    None
    """
    for lista in tabla:
        if lista is not None:
            asignar_mision_numero(lista, buscado, mision)
# ----------------------------------------------------------------------------------------------
