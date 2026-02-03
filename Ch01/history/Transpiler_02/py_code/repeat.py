numbers: list[int] = [0] * 10
number_index = 0
numbers[number_index] = int(input())
number_index += 1
numbers[number_index] = int(input())
max_idx = numbers[number_index]
for _ in range(max_idx):
    number_index -= 1
    value = numbers[number_index]
    print(chr(value), end='', flush=True)
    number_index += 1
    numbers[number_index] = numbers[number_index] - 1
