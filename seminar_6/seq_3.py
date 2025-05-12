import unittest

def count_seq_3(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    dp = {
        0: 1,
        1: 2,
        2: 4
    }
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]

class TestCountSeq3(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(count_seq_3(0), 1)
        self.assertEqual(count_seq_3(1), 2)
        self.assertEqual(count_seq_3(2), 4)

    def test_few_values(self):
        self.assertEqual(count_seq_3(3), 7)
        self.assertEqual(count_seq_3(4), 13)
        self.assertEqual(count_seq_3(5), 24)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCountSeq3)
runner = unittest.TextTestRunner()
runner.run(suite)
