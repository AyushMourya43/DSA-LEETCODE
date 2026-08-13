class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 2):

            # Duplicate i skip karo
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Left duplicates skip karo
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Right duplicates skip karo
                    # Yaha tum likho

                elif total < 0:
                    left += 1


                else:
                    right -= 1

        return ans