from pathlib import Path


def insert_tab(tab_count: int):
    tab_code = ""
    for _ in range(tab_count):
        tab_code += "    "
    return tab_code


if __name__ == "__main__":
    file_name = "./Ch01/bf_code/repeat.bf"

    with open(file_name, "r") as text_file:
        source_code: str = text_file.read()

    print(source_code)

    python_code = "numbers: list[int] = [0] * 10\n"
    python_code += "number_index = 0\n"

    tab_count = 0

    for code in source_code:
        match code:
            case ">":
                python_code += insert_tab(tab_count)
                python_code += "number_index += 1\n"
            case "<":
                python_code += insert_tab(tab_count)
                python_code += "number_index -= 1\n"
            case "+":
                python_code += insert_tab(tab_count)
                python_code += "numbers[number_index] = numbers[number_index] + 1\n"
            case "-":
                python_code += insert_tab(tab_count)
                python_code += "numbers[number_index] = numbers[number_index] - 1\n"
            case ".":
                python_code += insert_tab(tab_count)
                python_code += "value = numbers[number_index]\n"
                python_code += insert_tab(tab_count)
                python_code += "print(chr(value), end='', flush=True)\n"
            case ",":
                python_code += insert_tab(tab_count)
                python_code += "numbers[number_index] = int(input())\n"
            case "[":
                python_code += insert_tab(tab_count)
                python_code += "max_idx = numbers[number_index]\n"
                python_code += insert_tab(tab_count)
                python_code += "for _ in range(max_idx):\n"
                tab_count += 1
            case "]":
                tab_count -= 1

    print(python_code)

    filename_wo_ext = Path(file_name).stem
    with open(
        ".\\Ch01\\Transpiler\\py_code\\" + filename_wo_ext + ".py",
        "w",
    ) as python_file:
        python_file.write(python_code)
