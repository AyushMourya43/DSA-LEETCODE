class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = low +(high - low) // 2
            if nums[mid]== target:
                return mid

            elif nums[low] <= nums[mid]:   # Left half sorted hai
                   # Target left range me hai
                if nums[low] <= target < nums[mid]: 
                    high = mid -1

                else:
                    low = mid +1

            else: # nums[low] >= nums[mid].    # Right half sorted hai
                      # Target right range me hai
                 if nums[mid] < target <= nums[high]:
                    low = mid +1
                 else :
                    high = mid -1
        return -1                                 

        