class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.data = val
        self.left = left
        self.rights = right

def build_tree(arr, i):
    if i >= len(arr):
        return None
    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)

    return root
