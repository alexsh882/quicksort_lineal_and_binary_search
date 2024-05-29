def lineal_search(list: list, target: int):
    '''
    Función que devuelve el índice del elemento ingresado en el segundo parámetro.
    '''

    # Se recorre la lista y se compara cada elemento con el elemento buscado.
    # Si son iguales, se devuelve un mensaje con el elemento, el indice y cantidad de elementos totales.
    # Al final del ciclo, si no se encontró el elemento, se devuelve el mensaje.
    for i in range(len(list)):
        if list[i] == target:
            return f'El elemento {target} se encuentra en el índice {i}, de un total de {len(list)} elementos.'
    return f'No se encontró el elemento {target} en la lista.'
