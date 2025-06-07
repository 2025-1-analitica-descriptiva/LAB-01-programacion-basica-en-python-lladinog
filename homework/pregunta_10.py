"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.utils import get_column

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    column1 = get_column("files/input/data.csv", 0)
    column4 = get_column("files/input/data.csv", 3)
    column5 = get_column("files/input/data.csv", 4)

    result = []
    for letter, col4, col5 in zip(column1, column4, column5):
        count_col4 = len(col4.split(","))
        count_col5 = len(col5.split(","))
        result.append((letter, count_col4, count_col5))

    return result
