def is_symmetric(root):
    if root == None:
        return True
    queue = [root]

    while len(queue) > 0:
        queue_len = len(queue)
        for i in range(0, queue_len):
            if queue[i] is None and queue[queue_len -i - 1] is None:
                continue
            if queue[i] is None or queue[queue_len -i - 1] is None:
                return False
            if queue[i].data != queue[queue_len - i - 1].data:
                return False

            if queue[i] is not None:
                queue.append(queue[i].left)
                queue.append(queue[i].right)

        queue = queue[queue_len:]

    return True


def depth_search(root, res):
    if root == None:
        return res
    depth_search(root.left, res)
    res.append(root.data)
    depth_search(root.right, res)

    return res

def is_symmetric_DFS(root):
    if root == None:
        return True
    data = []
    data = depth_search(root, data)
    j = len(data) - 1
    for i in range(len(data)//2):
        if data[i] != data[j]:
            return False
        j -= 1
    return True
