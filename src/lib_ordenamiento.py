def ordenar_un_criterio(lista: list, key_uno: str):
    """ Ordena una lista de diccionarios por un criterio

    Args:
        lista  (list): lista de diccionarios
        key_uno (str): clave del criterio de ordenación

    Returns:
        list: lista ordenada de diccionarios
    """
    tam = len(lista)
    for i in range(0, tam - 1):
        for j in range(i + 1, tam):
            if lista[i][key_uno] < lista[j][key_uno]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista