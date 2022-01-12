def element_count(arr):
    fd = {}
    for s in arr:
        if s in fd.keys():
            fd[s] += 1
        else:
            fd[s] = 1
    return fd

print(element_count(["a", "b", "a", "a", "b"])) #=> {"a"=>3, "b"=>2}
print(element_count(["red", "red", "blue", "green"])) #=> {"red"=>2, "blue"=>1, "green"=>1}
#Write a method element_count that takes in an array and returns a hash representing the count of each element in the array.