"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.utils import get_column

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    column1 = get_column("files/input/data.csv", 0)
    column2 = get_column("files/input/data.csv", 1)

    result = {}
    for letter, value in zip(column1, column2):
        value = int(value)
        if letter not in result:
            result[letter] = [value, value]
        else:
            result[letter][0] = max(result[letter][0], value)
            result[letter][1] = min(result[letter][1], value)

    return [(k, v[0], v[1]) for k, v in sorted(result.items())]
