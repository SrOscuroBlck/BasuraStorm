class nodoLista(object):
    info, sig = None, None


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamano = 0


def insertar(lista, dato):
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
    return lista.inicio is None


def eliminar(lista, clave):
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
    return lista.tamano


def buscar(lista, buscado):
    aux = lista.inicio
    while(aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux


def barrido(lista):
    aux = lista.inicio
    while(aux is not None):
        print(aux.info)
        aux = aux.sig

def barrido_numero(lista, numero):
    aux = lista.inicio
    while(aux is not None):
        if aux.info["numero"][1:] == numero:
            print(aux.info)
        aux = aux.sig

def asignar_mision(lista, mision):
    aux = lista.inicio
    while(aux is not None):
        aux.info["mision"].append(mision)
        aux = aux.sig
        
def asignar_mision_numero(lista, numero, mision):
    aux = lista.inicio
    while(aux is not None):
        if aux.info["numero"][1:] == numero:
            aux.info["mision"].append(mision)
        aux = aux.sig
