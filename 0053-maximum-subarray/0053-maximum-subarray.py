class Solution(object):
    def maxSubArray(self, nums):
        
        current = nums[0]
        maximum = nums[0]

        for i in range(1,len(nums)):

            current = max(nums[i],current + nums[i])
            maximum = max(maximum , current)

        return maximum    
        
        # brute force
        # maximum = nums[0]
        
        # for i in range(len(nums)):
        #     current = 0

        #     for j in range(i,len(nums)):
        #         current += nums[j]
        #         maximum = max(maximum , current)

        # return maximum        