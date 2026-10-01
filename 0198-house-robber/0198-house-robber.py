class Solution(object):
    def rob(self, nums):
        
        if len(nums) == 1:
            return nums[0]

        prev1, prev2 = 0, 0

        for num in nums:
            prev1, prev2 = max(prev2 + num, prev1), prev1

        return prev1