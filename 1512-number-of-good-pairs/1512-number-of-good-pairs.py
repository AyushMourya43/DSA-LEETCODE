class Solution(object):
    def numIdenticalPairs(self, nums):
        
        freq = {}
        count = 0

        for num in nums:

             if num in freq:
                count += freq[num]
                freq[num] +=1

             else :
                freq[num] = 1

        return count         


# brute force 
#   count = 0

#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):

#                 if nums[i] == nums[j]:
#                     count += 1

#         return count
        