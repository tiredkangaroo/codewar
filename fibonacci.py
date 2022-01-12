def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    newArr = [1, 1]
    for s in range(n - 2):
        newArr.append(newArr[-2] + newArr[-1])
    return newArr

print(fibonacci(2))
print(fibonacci(6453))