def read_csv(file_path):
    """ 
    Reads a CSV file and returns its lines.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def csv_to_list(file_path):
    """
    Converts a CSV file to a list of lists, where each inner list represents a row.
    """
    lines = read_csv(file_path)
    return [line.strip().split("	") for line in lines]

def get_column(file_path, column):
    """
    Extracts a specific column from a CSV file and returns a list of values.
    """
    rows = csv_to_list(file_path)
    values = []
    for row in rows:
        if row:  # Skip empty rows
            value = row[column].strip()
            values.append(value)
    return values

def get_dictionary_column5():
    """
    Returns a dictionary where each key is a unique identifier from the fifth column
    of the CSV file, and each value is a list of integers representing the counts
    associated with that identifier.
    """
    column = get_column("files/input/data.csv", 4)
    dict = {}

    for entry in column:
        pairs = entry.split(",")
        for pair in pairs:
            key, value = pair.split(":")
            value = int(value)
            if key not in dict:
                dict[key] = [value]
            else:
                dict[key].append(value)

    return dict