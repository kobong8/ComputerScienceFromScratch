if __name__ == "__main__":
    file_name = "./Ch01/bf_code/repeat.bf"

    with open(file_name, "r") as text_file:
        source_code: str = text_file.read()

    print(source_code)

    python_code = "numbers: list[int] = [0] * 30000\n"
    python_code += "number_index = 0\n"

    tab_count = 0

    for code in source_code:
        for _ in range(tab_count):
            python_code += "    "

        match code:
            case ">":
                python_code += "number_index += 1\n"
            case "<":
                python_code += "number_index -= 1\n"
            case "+":
                python_code += "numbers[number_index] = numbers[number_index] + 1\n"
            case "-":
                python_code += "numbers[number_index] = numbers[number_index] - 1\n"
            case ".":
                python_code += "value = numbers[number_index]\n"
                python_code += "print(chr(value), end='', flush=True)\n"
            case ",":
                python_code += "numbers[number_index] = int(input())\n"
            case "[":
                python_code += "idx_max = numbers[number_index]\n"
                python_code += "for _ in range(idx_max):\n"
                tab_count += 1
            case "]":
                python_code += "\n"
                tab_count -= 1

        with open(
            ".\\Ch01\\Transpiler\\bf2py.py",
            "w",
        ) as python_file:
            python_file.write(python_code)
