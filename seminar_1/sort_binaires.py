def sortBinaries(arr):
    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] == 0:
            l += 1
        elif arr[r] == 1:
            r -= 1
        else: 
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    return arr

result = sortBinaries([0, 1, 1, 0, 1, 0, 1, 0])
result


def sortBinariesEnhanced(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] == 1:
            arr[l], arr[r] = arr[r], arr[l]
            r -= 1
        else:
            l += 1

    return arr

result = sortBinariesEnhances([0, 1, 1, 0, 1, 0, 1, 0])
result