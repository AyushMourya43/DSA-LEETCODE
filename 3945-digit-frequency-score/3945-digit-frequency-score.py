from collections import Counter 
class Solution(object):
    def digitFrequencyScore(self, n):
         freq = Counter(str(n))
         score =0

         for digit in freq :
            score += int (digit) * freq[digit]

         return score   
        