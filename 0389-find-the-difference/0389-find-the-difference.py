from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
       
        count_s = Counter(s)
        count_t = Counter(t)

        for ch in t:
            if count_s[ch] != count_t[ch]:
                return ch
        