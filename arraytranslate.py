def array_translate(array):
    fstr = ""
    for s in array:
        if type(s) is str:
            for i in range(array[array.index(s) + 1]):
                fstr += s
    return fstr

print(array_translate(["Cat", 2, "Dog", 3, "Mouse", 1])) # => "CatCatDogDogDogMouse"


print(array_translate(["red", 3, "blue", 1])) # => "redredredblue"
