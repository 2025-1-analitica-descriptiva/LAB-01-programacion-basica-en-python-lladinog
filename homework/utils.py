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
