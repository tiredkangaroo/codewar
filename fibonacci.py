def fibonacci(num):
    newArr = [1, 1]
    for s in range(num - 2):
        newArr.append(newArr[-2] + newArr[-1])
    return newArr

print(fibonacci(2))
print(fibonacci(6))