class Solution(object):
    def shortestToChar(self, s, c):
        
        ans = []
        for i in range(len (s)):
            min_distance = float("inf") # sabse badi value
           
            for j in range(len(s)):
                if s[j] == c:
                    min_distance = min(min_distance, abs(i - j))

            ans.append(min_distance)

        return ans