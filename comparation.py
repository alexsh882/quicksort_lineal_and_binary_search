import time
from lineal_search import lineal_search
from binary_search import binary_search

LISTA_LARGA = [f for f in range(1000)]
TARGET = 652


def time_function(func, *args):
    '''
    Función que mide el tiempo de ejecución de una función e muestra por consola el resultado en segundos.
    '''
    start_time = time.perf_counter()
    print(func(*args))
    end_time = time.perf_counter()
    return print(f'Tiempo de ejecución de la función {func.__name__}: {end_time - start_time} segundos.')

print(f'\nComprobación de búsqueda binaria')
time_function(binary_search, LISTA_LARGA, TARGET)

print(f'\nComprobación de búsqueda lineal')
time_function(lineal_search, LISTA_LARGA, TARGET)

