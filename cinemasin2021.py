def maximum_seating(array):
    def legal(arr):
        for idx, ele in enumerate(arr):
            if ele == 1:
                if idx + 2 <= len(arr):
                    if arr[idx + 1] == 1 or arr[idx + 2] == 1:
                        return False
        return True
    
    addables = 0
    for idx, ele in enumerate(array):
        if array[idx] == 0:
            array[idx] = 1
            if legal(array):
                addables += 1
            else:
                array[idx] = 0
    return addables
print(maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0])) #2
print(maximum_seating([0, 0, 0, 0])) #2
print(maximum_seating([1, 0, 0, 0, 0, 1])) #0
