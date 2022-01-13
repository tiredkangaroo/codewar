<<<<<<< HEAD
def fibonacci(num):
    newArr = [1, 1]
    for s in range(num - 2):
=======
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    newArr = [1, 1]
    for s in range(n - 2):
>>>>>>> 0722d8d430d59f7a4843e8ef8c624d39b5af0f87
        newArr.append(newArr[-2] + newArr[-1])
    return newArr

print(fibonacci(2))
<<<<<<< HEAD
print(fibonacci(6))
=======
print(fibonacci(6453))
>>>>>>> 0722d8d430d59f7a4843e8ef8c624d39b5af0f87
