class Solution(object):
    def productExceptSelf(self, nums):
        
        ans = [1] * len(nums)

        left = 1

        for i in range(len(nums)):
            ans[i] = left
            left *= nums[i]

        right = 1

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans

        # Brute force 
        # for i in range(len(nums)):
        #     product = 1

        #     for j in range(len(nums)):
        #          if i != j:
        #          product *= nums[j]

        #      ans.append(product)