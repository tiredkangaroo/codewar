def descending_order(num):
    numl = [m for m in str(num)]
    numl.sort()
    numl.reverse()
    return int("".join(numl))
print(descending_order(32456452145))