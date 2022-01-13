def yell_sentence(sent):
    return " ".join(list(map(lambda x: x.upper() + "!", sent.split())))

print(yell_sentence("I have a bad feeling about this")) #=> "I! HAVE! A! BAD! FEELING! ABOUT! THIS!"