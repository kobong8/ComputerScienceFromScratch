from pathlib import Path


class Transpiler:
    def __init__(self, file_name: str | Path):
        # Open text file and store in instance variable
        with open(file_name, "r") as text_file:
            self.source_code: str = text_file.read()

    def execute(self):
        # Setup state
        cells: list[int] = [0] * 30000
        cell_index = 0
        instruction_index = 0

        py_code = ""
        py_code += "numbers: list[int] = [0] * 30000\n"
        py_code += "number_index = 0\n"

        # Keep going as long as there are potential instructions left
        while instruction_index < len(self.source_code):
            instruction = self.source_code[instruction_index]
            match instruction:
                case ">":
                    cell_index += 1
                    py_code += "number_index += 1\n"
                case "<":
                    cell_index -= 1
                    py_code += "number_index -= 1\n"
                case "+":
                    cells[cell_index] = clamp0_255_wraparound(cells[cell_index] + 1)
                    py_code += "numbers[number_index] = numbers[number_index] + 1\n"
                case "-":
                    cells[cell_index] = clamp0_255_wraparound(cells[cell_index] - 1)
                    py_code += "numbers[number_index] = numbers[number_index] - 1\n"
                case ".":
                    print(chr(cells[cell_index]), end="", flush=True)
                    py_code += 'print(chr(numbers[number_index]), end="", flush=True)\n'
                case ",":
                    cells[cell_index] = clamp0_255_wraparound(int(input()))
                    py_code += "numbers[number_index] = int(input())\n"
                case "[":
                    if cells[cell_index] == 0:
                        instruction_index = self.find_bracket_match(
                            instruction_index, True
                        )
                        py_code += ""
                case "]":
                    if cells[cell_index] != 0:
                        instruction_index = self.find_bracket_match(
                            instruction_index, False
                        )
                        py_code += ""

            instruction_index += 1

        with open(
            ".\\bf2py.py",
            "w",
        ) as py_file:
            py_file.write(py_code)

    # Find the location of the corresponding bracket to the one at *start*
    # If *forward* is true go to the right looking for a matching "]"
    # Otherwise do the reverse
    def find_bracket_match(self, start: int, forward: bool) -> int:
        in_between_brackets = 0
        direction = 1 if forward else -1
        location = start + direction
        start_bracket = "[" if forward else "]"
        end_bracket = "]" if forward else "["
        while 0 <= location < len(self.source_code):
            if self.source_code[location] == end_bracket:
                if in_between_brackets == 0:
                    return location
                in_between_brackets -= 1
            elif self.source_code[location] == start_bracket:
                in_between_brackets += 1
            location += direction
        # Didn't find a match
        print(f"Error: could not find match for {start_bracket} at {start}.")
        return start


# Simulate a 1 byte unsigned integer
def clamp0_255_wraparound(num: int) -> int:
    if num > 255:
        return 0
    elif num < 0:
        return 255
    else:
        return num
