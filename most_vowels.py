def most_vowels(sentence):
    currentWord = ["", 0]
    for s in sentence.split():
        vowels = 0
        for i in s:
            if i in "aeiou":
                vowels += 1
        if vowels > currentWord[1]:
            currentWord = [s, vowels]
    return currentWord[0]
print(most_vowels("what a wonderful life")) #=> "wonderful"