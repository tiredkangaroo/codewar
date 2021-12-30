def two_d_translate(arr):
    farr = []
    for s in arr:
        for i in range(s[1]):
            farr.append(s[0])
    return farr

arr_1 = [
  ['boot', 3],
  ['camp', 2],
  ['program', 0]
]

print(two_d_translate(arr_1)) # => [ 'boot', 'boot', 'boot', 'camp', 'camp' ]

arr_2 = [
  ['red', 1],
  ['blue', 4]
]

print(two_d_translate(arr_2)) # => [ 'red', 'blue', 'blue', 'blue', 'blue' ]