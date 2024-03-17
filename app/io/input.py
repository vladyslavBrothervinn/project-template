import pandas as pd


def input_from_keyboard():
    """
    Performs a functions that gets an input of the user and returns it as a string.

    No Args or Kwargs.

    Returns:
        string: The text that user entered.
    """
    print("Enter the text, please")
    string = input()
    return string


def read_file(path_to_file):
    """
    Performs a reading from the file using a path to it as an argument. Gets printed out and returned.

    :arg: path_to_file(string). The only parameter, is a path to the located file to get read.

    :return: string. It contains the text that is in the file.
    """
    with open(path_to_file, 'r') as reader:
        file = reader.read()
        return file


def read_file_pandas(path_to_file):
    """
    Performs a reading from the file using a path to it as an argument. Gets printed out and returned.
    Uses pandas utilities to read the file.

    :arg: path_to_file(string). The only parameter, is a path to the located file to get read.

    :return: string. It contains the text that is in the file.
    """
    df = pd.read_csv(path_to_file, sep=' ')

    return df
