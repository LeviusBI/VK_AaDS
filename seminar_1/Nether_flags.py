def netherFlag(arr):
    l = 0 
    m = 0
    h = len(arr) - 1
    while m < h:
        if arr[m] == 2:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
        elif arr[m] == 0:
            arr[m], arr[l] = arr[l], arr[m]
            l += 1
            m += 1
        else:
            m += 1
    return arr

result = netherFlag([2, 0, 2, 1, 1, 0])
result