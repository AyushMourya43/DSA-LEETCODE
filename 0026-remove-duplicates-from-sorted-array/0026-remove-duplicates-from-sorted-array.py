class Solution(object):
    def removeDuplicates(self, nums):
        
        n = len(nums)

        i = 0

        if len(nums) == 0:
            return 0
            
        for j in range(1,n):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i =i+1

        return(i+1)       
        
        