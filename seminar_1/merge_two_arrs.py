def mergeSortedArrs(arr1, arr2):
    first = len(arr1) - len(arr2) - 1
    second = len(arr2) - 1
    third = len(arr1) - 1
    while second >= 0:
        if first >= 0 and arr1[first] > arr2[second]:
            arr1[third] = arr1[first]
            first -= 1
        else:
            arr1[third] = arr2[second]
            second -= 1
        third -= 1
    return arr1

result = mergeSortedArrs([3, 8, 10, 11, 0, 0, 0], [1, 7, 9])
result