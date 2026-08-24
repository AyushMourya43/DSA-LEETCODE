class Solution(object):
    def moveZeroes(self, nums):
       
       z = 0
       i = 0

       while i < (len(nums)):
        if nums[i] != 0:
            nums[z],nums[i] = nums[i],nums[z]
            z +=1
        i +=1
            
