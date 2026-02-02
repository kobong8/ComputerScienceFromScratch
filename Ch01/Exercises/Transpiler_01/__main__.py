from argparse import ArgumentParser
from Transpiler.transpiler import Transpiler

if __name__ == "__main__":
    # Parse the file argument
    file_parser = ArgumentParser("Brainfuck")
    file_parser.add_argument(
        "brainfuck_file", help="A file containing Brainfuck source code."
    )
    arguments = file_parser.parse_args()
    Transpiler(arguments.brainfuck_file).execute()
