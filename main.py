from app.io import input
from app.io import output


def main():

    PATH_TO_INPUT_V1 = "data/input.txt"

    PATH_TO_INPUT_V2 = "data/input_v2"

    string1 = input.input_from_keyboard()
    print(string1+'\n')

    string2 = input.read_file(PATH_TO_INPUT_V1)
    print(string2+'\n')

    string3 = input.read_file_pandas(PATH_TO_INPUT_V2)
    print(string3)
    print()

    string4 = "this text is going to be printed!"
    output.to_print(string4+'\n')

    string5 = "One day Luffy D. Monkey is going to become the king of the pirates!"
    output.write_to_file(string5, "data/output.txt")


if __name__ == "__main__":
    main()
