class Solution(object):
    def findDuplicate(self, nums):
       slow = 0 
       fast = 0

       while True:

        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break
       finder = 0     

       while finder != slow:

        finder = nums[finder]
        slow = nums[slow]

       return finder    
       
            # brute force
    #    for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #            if nums[i] == nums[j]:
    #               return nums[i]