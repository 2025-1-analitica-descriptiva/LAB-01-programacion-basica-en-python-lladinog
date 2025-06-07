"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.utils import get_column

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    column1 = get_column("files/input/data.csv", 0)
    column5 = get_column("files/input/data.csv", 4)

    result = {}
    for key, value in zip(column1, column5):
        for pair in value.split(","):
            _, val = pair.split(":")
            result[key] = result.get(key, 0) + int(val)

    return dict(sorted(result.items()))

