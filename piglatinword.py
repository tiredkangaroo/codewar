# Pig latin translation uses the following rules:
# - for words that start with a vowel, add 'yay' to the end
# - for words that start with a nonvowel, move all letters before the first vowel to the end of the word and add 'ay'

def pig_latin_word(word):
    fword = ""
    if word[0] in ["a", "e", "i", "o", "u"]:
        fword = word + "yay"
    else:
        idx = 0
        for s in word:
            if s in ["a", "e", "i", "o", "u"]:
                idx = word.index(s)
        for s in word[idx:]:
            fword += s
        fword += word[0] + "ay"
    return fword

print(pig_latin_word("apple"))   # => "appleyay"
print(pig_latin_word("eat"))     # => "eatyay"
print(pig_latin_word("banana"))  # => "ananabay"
print(pig_latin_word("trash"))   # => "ashtray"