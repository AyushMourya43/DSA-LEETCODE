class Solution(object):
    def twoSum(self, nums, target):

       n = len(nums)
       seen = {}

       for i in range(0,n):
         need = target - nums[i] # remaining jo  bacchaa woh

         if need in seen:
            return[seen[need],i]

         seen[nums[i]] = i   

# brute force
#  for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]


