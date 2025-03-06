def is_palindrom(s, type_of_algo='2_pointers'):
    if type_of_algo == '2_pointers':
        left = 0
        right = len(s) - 1

        while (left < right):
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    elif type_of_algo == 'stack':
        stack = Stack()
        for i in s:
            stack.push(i)
        for i in s:
            if i != stack.pop():
                return False
        return True