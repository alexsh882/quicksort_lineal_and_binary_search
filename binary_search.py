def binary_search(list: list, target: int):
    '''
    Función que devuelve el índice del elemento ingresado en el segundo parámetro.
    '''
    left_index = 0
    right_index = len(list) - 1

    # Mientras el índice izquierdo sea menor o igual al derecho, se ejecutará el ciclo.
    while left_index <= right_index:

        # Se calcula el índice medio.
        middle = left_index + (right_index - left_index) // 2

        # Se compara el elemento en el índice medio con el elemento buscado.
        # Si son iguales, se devuelve un mensaje con el elemento, el indice y cantidad de elementos totales.
        # Si no son iguales, se actualiza el índice izquierdo o derecho según sea el caso.
        # Al final del ciclo, si no se encontró el elemento, se devuelve el mensaje.
        if list[middle] == target:
            return f'El elemento {target} se encuentra en el índice {middle}, de un total de {len(list)} elementos.'
        # Si el elemento en el índice medio es menor al elemento buscado, se actualiza el índice izquierdo.
        elif list[middle] < target:
            left_index = middle + 1
        # Si el elemento en el índice medio es mayor al elemento buscado, se actualiza el índice derecho.
        else:
            right_index = middle - 1

    return f'No se encontró el elemento {target} en la lista.'

# Prueba de la función

LISTA_LARGA = [0, 1, 2, 8, 13, 17, 19, 32, 42, 44, 54, 62, 68, 77, 82, 87]
TARGET = 82

print(binary_search(LISTA_LARGA, TARGET))