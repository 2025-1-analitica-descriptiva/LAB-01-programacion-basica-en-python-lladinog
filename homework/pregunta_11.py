"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.utils import get_column

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    column2 = get_column("files\input\data.csv", 1)
    column4 = get_column("files\input\data.csv", 3)

    result = {}
    for text, value in zip(column4, column2):
        letters = text.split(",")
        for letter in letters:
            result[letter] = result.get(letter, 0) + int(value)

    return dict(sorted(result.items()))
