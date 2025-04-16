def diff_two(a, b):
    map_a = {}
    
    for symbol in a:
        map_a[symbol] = map_a.get(symbol, 0) + 1
    
    for symbol in b:
        if symbol in map_a:
            map_a[symbol] -= 1
            if map_a[symbol] == 0:
                del map_a[symbol]
        else:
            return symbol
    
    return ""


class TestDiffTwo(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(diff_two("abcd", "abcde"), "e")
        self.assertEqual(diff_two("a", "aa"), "a")

    def test_edge_cases(self):
        self.assertEqual(diff_two("", "z"), "z")
        self.assertEqual(diff_two("xyz", "xzya"), "a")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)