class Solution(object):
    def isAnagram(self, s, t):

        return sorted(s) == sorted(t)
    # sorting timecomplexity is O(n log n )


# it is optimal ( hashmap )
# if len(s) != len(t):
#             return False

#         count = {}

#         for ch in s:
#             count[ch] = count.get(ch, 0) + 1

#         for ch in t:

#             if ch not in count:
#                 return False

#             count[ch] -= 1

#             if count[ch] < 0:
#                 return False

#         return True