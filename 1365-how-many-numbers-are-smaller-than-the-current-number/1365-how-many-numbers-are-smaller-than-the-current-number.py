class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
        sorted_nums = sorted(nums)

        mp={}

        for i , num in enumerate(sorted_nums):
            if num not in mp:
                mp[num]=i

        ans=[]

        for num in nums:
            ans.append(mp[num])

        return ans    

# brute force
#  ans = []

#         for i in range(len(nums)):
#             count = 0

#             for j in range(len(nums)):
#                 if nums[j] < nums[i]:
#                     count += 1

#             ans.append(count)

#         return ans