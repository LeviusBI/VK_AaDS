def b_seq(n, use_dp=True):
    def recursion(n):
        if n == 1:
            return 2
        if n == 2:
            return 3
        return recursion(n - 1) + recursion(n - 2)

    def din_prog(n):
        dp = {
            0: 1,
            1: 2
        }
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    if use_dp:
        return din_prog(n)
    else:
        return recursion(n)

import unittest

class TestBSeq(unittest.TestCase):
    def test_recursive(self):
        self.assertEqual(b_seq(1, use_dp=False), 2)
        self.assertEqual(b_seq(2, use_dp=False), 3)
        self.assertEqual(b_seq(5, use_dp=False), 13)

    def test_dp(self):
        self.assertEqual(b_seq(1, use_dp=True), 2)
        self.assertEqual(b_seq(2, use_dp=True), 3)
        self.assertEqual(b_seq(5, use_dp=True), 13)

suite = unittest.TestLoader().loadTestsFromTestCase(TestBSeq)
runner = unittest.TextTestRunner()
runner.run(suite)