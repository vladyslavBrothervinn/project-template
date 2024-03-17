
def to_print(string):
    """
    Performs an output of the given text
    :arg: string: the only argument that gets printed out
    :return: None
    """
    print(string)
    return None


def write_to_file(text, file_to_path):
    """
    Performs a save of the text to the given file
    :arg: text: string. First argument contains the text that will be saved to the certain file.
    :arg: file_to_path: string. Second argument contains the path to the fill where the text will be saved
    :return: None
    """
    with open(file_to_path, 'w') as writer:
        writer.write(text)

    print("Successfully saved!")
