numbers: list[int] = [0] * 30000
number_index = 0
numbers[number_index] = int(input())
number_index += 1
numbers[number_index] = int(input())
idx_max = numbers[number_index]
for _ in range(idx_max):
    number_index -= 1
    value = numbers[number_index]
    print(chr(value), end="", flush=True)
    number_index += 1
    numbers[number_index] = numbers[number_index] - 1
