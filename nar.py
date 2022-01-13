def nar(value):
    valuespl = [s for s in str(value)]
    finalval = 0
    for s in valuespl:
        finalval += int(s) ** len(valuespl)
    return finalval == value

print(nar(153))
print(nar(52))
print(nar(5))
print(nar(1633))