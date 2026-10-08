class Solution(object):
    def missingNumber(self, nums):
           n = len(nums)

           for i in range(n + 1):
              if i not in nums:
                return i

    #     n = len(nums)
    #  Expected Sum - Actual Sum = Missing Number
    # n(n+1)
    # _______
    #   2
    #     expected = n * (n + 1) // 2
    #     actual = sum(nums)

    #     return expected - actual
	# ​
