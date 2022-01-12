def o_words(sentence):
    return [s for s in sentence.split() if "o" in s]
print(o_words("How did you do that?")) #=> ["How", "you", "do"]