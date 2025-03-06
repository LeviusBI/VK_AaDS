def reverseArray(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr
reverted = reverseArray([3, 8, 6, 9, 9, 8, 6])
reverted