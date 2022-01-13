def whisper_words(words):
    return list(map(lambda word: word.lower() + "...", words))

print(whisper_words(["KEEP", "The", "NOISE", "down"])) # => ["keep...", "the...", "noise...", "down..."]