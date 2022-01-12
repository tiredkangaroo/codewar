def last_index(string, char):
    lastindex = 0
    for s in range(len(string)):
        if string[s] == char:
            lastindex = s
    return lastindex
print(last_index("abca", "a"))       #=> 3
print(last_index("mississipi", "i")) #=> 9
print(last_index("octagon", "o"))    #=> 5
print(last_index("programming", "m"))#=> 7