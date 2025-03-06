def mooveEven(arr):
    f = 0
    s = 0
    while s <= len(arr) - 1:
        if arr[s] % 2 == 0:
            arr[s], arr[f] = arr[f], arr[s]
            f += 1
            s += 1
        else:
            s += 1
    return arr

result = mooveEven([3, 2, 4, 1, 11, 8, 9])
result