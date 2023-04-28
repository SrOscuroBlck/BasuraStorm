class nodoLista(object):
    """
    Clase nodoLista, representa un nodo en una lista enlazada.
    
    Atributos:
    - info: información almacenada en el nodo.
    - sig: referencia al siguiente nodo de la lista enlazada.
    """
    info, sig = None, None


class Lista(object):
    """
    Clase Lista, representa una lista enlazada.
    
    Atributos:
    - inicio: referencia al primer nodo de la lista enlazada.
    - tamano: cantidad de elementos en la lista.
    """
    def __init__(self):
        """
        Constructor de la clase Lista.
        """
        self.inicio = None
        self.tamano = 0


def insertar(lista, dato):
    """
    Inserta un dato en la lista enlazada.
    
    Parámetros:
    - lista: instancia de la clase Lista en la que se va a insertar el dato.
    - dato: información que se va a almacenar en el nodo.
    """
    nodo = nodoLista()
    nodo.info = dato
    if (lista.inicio is None) or (lista.inicio.info["numero"] > dato["numero"]):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while(act is not None and act.info["numero"] < dato["numero"]):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamano += 1


def lista_vacia(lista):
    """
    Determina si una lista enlazada está vacía o no.
    
    Parámetros:
    - lista: instancia de la clase Lista que se desea evaluar.
    
    Retorna: True si la lista está vacía, False si no lo está.
    """
    return lista.inicio is None


def eliminar(lista, clave):
    """
    Elimina un nodo de la lista enlazada, dado un valor de clave.
    
    Parámetros:
    - lista: instancia de la clase Lista en la que se va a eliminar el nodo.
    - clave: valor de la clave del nodo que se desea eliminar.
    
    Retorna: el dato almacenado en el nodo eliminado, o None si no se encontró.
    """
    dato = None
    if(lista.inicio.info["numero"] == clave):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamano -= 1
    else:
        anterior = lista.inicio
        actual = lista.inicio.sig
        while(actual is not None and actual.info["numero"] != clave):
            anterior = anterior.sig
            actual = actual.sig
        if(actual is not None):
            dato = actual.info
            anterior.sig = actual.sig
            lista.tamano -= 1
    return dato


def tamano(lista):
    """
    Retorna la cantidad de elementos en una lista enlazada.
    
    Parámetros:
    - lista: instancia de la clase Lista que se desea evaluar.
    
    Retorna: un entero que indica la cantidad de elementos en la lista.
    """
    return lista.tamano


def buscar(lista, buscado):
    """
    Busca un elemento en una lista enlazada.

    Parameters:
    lista (Lista): la lista enlazada donde buscar el elemento.
    buscado (object): el elemento a buscar.

    Returns:
    nodoLista: el nodo que contiene el elemento buscado, o None si no se encuentra.
    """
    aux = lista.inicio
    while(aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux


def barrido(lista):
    """
    Recorre la lista enlazada e imprime cada elemento.

    Parameters:
    lista (Lista): la lista enlazada a recorrer.
    """
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig


def barrido_numero(lista, numero):
    """
    Recorre la lista enlazada e imprime los elementos cuyo número termine en el número especificado.

    Parameters:
    lista (Lista): la lista enlazada a recorrer.
    numero (str): el número de tres dígitos a buscar al final de cada número.

    """
    aux = lista.inicio
    while(aux is not None):
        if aux.info["numero"][-3:] == numero:
            print(aux.info)
        aux = aux.sig


def asignar_mision(lista, mision):
    """
    Asigna una misión a todos los elementos de una lista enlazada.

    Parameters:
    lista (Lista): la lista enlazada a recorrer y asignar la misión.
    mision (str): la misión a asignar.

    """
    aux = lista.inicio
    while(aux is not None):
        aux.info["misiones"].append(mision)
        aux = aux.sig
        
        
def asignar_mision_numero(lista, numero, mision):
    """
    Asigna una misión a todos los elementos de una lista enlazada que tengan un númerso que termine en el número especificado.

    Parameters:
    lista (Lista): la lista enlazada a recorrer y asignar la misión.
    numero (str): el número de tres dígitos a buscar al final de cada número.
    mision (str): la misión a asignar.

    """
    aux = lista.inicio
    while(aux is not None):
        if aux.info["numero"][-3:] == numero:
            aux.info["misiones"].append(mision)
        aux = aux.sig
