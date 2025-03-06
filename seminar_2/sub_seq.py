def is_subseq(a, b):
    q = Queue()
    for i in a:
        q.push(i)
    a_data = q.pop()
    for j in b:
        if a_data == j:
            a_data = q.pop()


    return q.size == 0
a = 'abd'
b = 'uabqd'
if is_subseq(a, b):
    print('yep')
else:
    print('nope')
        