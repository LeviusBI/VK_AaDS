import unittest

def binary_search_sqrt(target):
    l = 0
    r = target
    while l <= r:
        middle = l + (r - l) // 2
        if middle ** 2 > target:
            r = middle - 1
            continue
        if middle ** 2 < target:
            l = middle + 1
            continue
        return middle
    return r  

class TestBinarySearchSqrt(unittest.TestCase):

    def test_round_squares(self):
        self.assertEqual(binary_search_sqrt(0), 0)  
        self.assertEqual(binary_search_sqrt(1), 1) 
        self.assertEqual(binary_search_sqrt(4), 2)  
        self.assertEqual(binary_search_sqrt(16), 4)  

    def test_non_round_squares(self):
        self.assertEqual(binary_search_sqrt(2), 1)  
        self.assertEqual(binary_search_sqrt(3), 1)  
        self.assertEqual(binary_search_sqrt(5), 2) 


    def test_edge_cases(self):
        self.assertEqual(binary_search_sqrt(0), 0)
        self.assertEqual(binary_search_sqrt(1), 1)  
        self.assertEqual(binary_search_sqrt(2), 1)  

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)