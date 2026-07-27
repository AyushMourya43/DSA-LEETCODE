class Solution(object):
    def findMin(self, nums):
        
        low = 0
        high = len(nums)-1

        while low < high:
            
            mid = low+ (high - low)//2

            if nums[mid] >= nums[high]: # agr aisa h toh roated array h # to minimum right side me hoga.
                low = mid +1

            else:
               high = mid       # to right part sorted hai.
                                # Minimum left side ya mid khud ho sakta hai.  

        return nums[low]                          
  
