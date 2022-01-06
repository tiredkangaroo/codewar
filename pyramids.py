# For example, the base [1, 4, 6] gives us the following pyramid
#     15
#   5   10
# 1   4    6
def simplify(base):
    newArr = []
    i = 0
    for s in base:
        if i < len(base) - 1:
            newArr.append(s + base[i + 1])
        i += 1
    return newArr

def pyramids(base):
    farr = [base]
    # farr.append(simplify(base))
    i = 0
    while len(farr[-1]) > 1:
        farr.append(simplify(farr[-1]))
        i += 1
    farr.reverse()
    return farr


print(pyramids([1, 4, 6]))  #=> [[15], [5, 10], [1, 4, 6]]
print("\n")
print(pyramids([3, 7, 2, 11])) #=> [[41], [19, 22], [10, 9, 13], [3, 7, 2, 11]]