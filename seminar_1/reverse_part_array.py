def reverseArray(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
        
def reversePartArray(arr, k):
    n = len(arr)
    arr = reverseArray(arr, 0, n - 1)
    arr = reverseArray(arr, 0, k % n - 1)
    arr = reverseArray(arr, k % n, n - 1)
    return arr

result1 = reversePartArray([1, 2, 3, 4, 5, 6, 7], 3)
result2 = reversePartArray([1, 2, 3, 4, 5, 6, 7], 8)
result1, result2