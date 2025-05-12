def coin_change_dp(coins, amount):
    dp = {}
    for i in range(amount + 1):
        dp[i] = float('inf')
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == float('inf') else dp[amount]
import unittest

class TestCoinChange(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(coin_change_dp([1, 2, 5], 11), 3)

    def test_no_solution(self):
        self.assertEqual(coin_change_dp([2], 3), -1)
        self.assertEqual(coin_change_dp([2, 5], 3), -1)

    def test_zero_amount(self):
        self.assertEqual(coin_change_dp([1, 2, 5], 0), 0)

    def test_one_coin(self):
        self.assertEqual(coin_change_dp([1], 2), 2)
        
suite = unittest.TestLoader().loadTestsFromTestCase(TestCoinChange)
runner = unittest.TextTestRunner()
runner.run(suite)
