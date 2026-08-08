class Solution(object):
    def convertToTitle(self, columnNumber):
        
        ans = ""

        while columnNumber > 0:   # A=65 , a = 97
            columnNumber -=1
            ans = chr(columnNumber % 26 + ord('A')) + ans
            columnNumber //= 26

        return ans    
