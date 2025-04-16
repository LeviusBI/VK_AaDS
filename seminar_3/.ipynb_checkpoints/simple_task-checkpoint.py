import unittest

def copy_time(n, x, y):
    l = 0
    r = (n - 1) * max(x, y)

    
    while l + 1 < r:
        mid = (l + r) // 2
        if (mid // x) + (mid // y) < n - 1:  
            l = mid
        else:
            r = mid

    return r + min(x, y)

class TestCopyTime(unittest.TestCase):

    def test_single_sheet(self):
        self.assertEqual(copy_time(5, 1, 2), 5) 

    def test_small_n(self):
        self.assertEqual(copy_time(1, 2, 3), 2) 

    def test_large_n(self):
        self.assertEqual(copy_time(10, 4, 6), 24) 
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)