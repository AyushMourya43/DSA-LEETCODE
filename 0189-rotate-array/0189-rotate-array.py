class Solution(object):
    def rotate(self, nums, k):
        #  n = len(nums)
        #  k = k % n

        #  for j in range(k):
        #      temp = nums[0]

        #      for i in range(1,n):
        #         nums[i-1] = nums[i]
        #      nums[n-1] = temp

        #  return nums      

        n = len(nums)
        k = k % n

        def reverse(left , right):
            while left < right:
              nums[left] , nums[right] = nums[right] , nums[left]
              left +=1
              right -=1

        reverse(0,n-1) # full reverse
        reverse(0,k-1) #  k places reverse
        reverse(k,n-1) # remaiang reverse



