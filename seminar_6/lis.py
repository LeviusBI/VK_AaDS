import unittest

def find_lis(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            dp[i] = dp[i - 1] + 1

    return max(dp)

class TestFindLIS(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_lis([]), 0)

    def test_single_element(self):
        self.assertEqual(find_lis([5]), 1)

    def test_all_increasing(self):
        self.assertEqual(find_lis([1, 2, 3, 4, 5]), 5)

    def test_all_equal(self):
        self.assertEqual(find_lis([2, 2, 2, 2]), 1)

    def test_all_decreasing(self):
        self.assertEqual(find_lis([5, 4, 3, 2, 1]), 1)

    def test_mixed_values(self):
        self.assertEqual(find_lis([1, 3, 2, 4, 6, 5]), 3)

    def test_peak_and_valley(self):
        self.assertEqual(find_lis([7, 10, 12, 13, 8, 9]), 4)


suite = unittest.TestLoader().loadTestsFromTestCase(TestFindLIS)
runner = unittest.TextTestRunner()
runner.run(suite)
