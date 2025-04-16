import unittest
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def minDepth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is not None and root.right is not None:
        return 1 + min(minDepth(root.left), minDepth(root.right))
    if root.left is not None:
        return 1 + minDepth(root.left)
    if root.right is not None:
        return 1 + minDepth(root.right)

class TestMinDepth(unittest.TestCase):

    def test_simple_cases(self):
        root = TreeNode(1)
        self.assertEqual(minDepth(root), 1)

        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        self.assertEqual(minDepth(root), 2)

    def test_edge_cases(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(minDepth(root), 3)

        root = None
        self.assertEqual(minDepth(root), 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
