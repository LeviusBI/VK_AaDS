def badToEnd(arr):
    first = 0
    second = 0 
    while second <= len(arr) - 1:
        if arr[first] == 0 and arr[second] == 0:
            second += 1
        elif arr[second] != 0:
            arr[first], arr[second] = arr[second], arr[first]
            first += 1
    return arr
result = badToEnd([0, 0, 1, 0, 3, 12])
result 

result = badToEnd([0, 33, 57, 88, 60, 0, 0, 80, 99])
result