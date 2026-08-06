class Solution(object):
    def sortArrayByParity(self, nums):
        
        left = 0
        right = len(nums) - 1

        while left < right:

            if nums[left] % 2 == 0:
                left += 1

            elif nums[right] % 2 == 1:
                right -= 1

            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums

        #brute force
        # even = []
        # odd = []

        # for num in nums:
        #     if num % 2 == 0:
        #         even.append(num)
        #     else:
        #         odd.append(num)

        # return even + odd