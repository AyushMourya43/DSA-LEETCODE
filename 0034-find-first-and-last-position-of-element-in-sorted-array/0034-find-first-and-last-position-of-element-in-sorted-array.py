class Solution(object):
    def searchRange(self, nums, target):
        
        first = -1
        last = -1

        low =0           # first occurence left jaaoo left m dhuundo 
        high = len(nums)-1

        while low <= high:  
          
           mid = low+(high - low) // 2

           if nums[mid] == target:
               first = mid
               high = mid - 1

           elif nums[mid] < target:
                low = mid +1
           else:
                high = mid -1     
                  
        low =0           # last occurence right jaaoo right m dhuundo 
        high = len(nums)-1
        
        while low <= high:
           mid = low+(high - low) // 2

           if nums[mid] == target:
               last = mid
               low = mid + 1

           elif nums[mid] < target:
                low = mid +1
           else:
                high = mid -1     

        return [first , last]        

