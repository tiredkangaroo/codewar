def binary_array_to_number(arr):
    return int("".join(str(e) for e in arr), 2)
print(binary_array_to_number([0, 1, 2, 1]))