class Solution(object):
    def sortedSquares(self, nums):
        
        n = len(nums)
        ans = [0] * n

        left = 0
        right = n - 1
        pos = n - 1      # ans length

        while left <= right:

            if nums[left] ** 2 > nums[right] ** 2:
                ans[pos] = nums[left] ** 2
                left += 1
            else:
                ans[pos] = nums[right] ** 2
                right -= 1

            pos -= 1

        return ans


        # brute force 
        # ans = []

        # for num in nums:
        #     ans.append(num * num)

        # ans.sort()
        # return ans