def descending_order(num):
    numl = [m for m in str(num)]
    numl.sort()
    numl.reverse()
    return int("".join(numl))
print(descending_order(32456452145))

# Pulled from another solution, we could've done:
# numl.sort(reverse=True) which auto reverses it, making it 3, 2, 1 instead of 1, 2, 3
# We could also make it a one-liner:
# return int("".join([m for m in str(num)].sort(reverse=True)))
# Pulled from another solution, we could've used the sorted function for a string instead of using .sort for an array
# return int("".join(sorted(str(num), reverse=True))
# Remember, sorted return an array of the sorted string, not a string, so we can't just do int(sorted(str(num), reverse=True))