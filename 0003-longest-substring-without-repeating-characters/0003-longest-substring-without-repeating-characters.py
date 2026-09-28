class Solution(object):
    def lengthOfLongestSubstring(self, s):
       
       my_set = set()
       left = 0
       maxi = 0

       for right in range(len(s)):
           
           while s[right] in my_set:
              my_set.remove(s[left])
              left +=1

           my_set.add(s[right])

           maxi = max(maxi,right-left+1)

       return maxi      