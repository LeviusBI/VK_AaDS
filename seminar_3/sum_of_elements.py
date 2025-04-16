def twoSum(data, target):
    cache = {}  
    for i in range(len(data)):
        diff = target - data[i] 
        if diff in cache: 
            return [cache[diff], i]
        cache[data[i]] = i 
    return [] 