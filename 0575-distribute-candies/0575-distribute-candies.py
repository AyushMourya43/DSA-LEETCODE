class Solution(object):
    def distributeCandies(self, candyType):

        unique = len(set(candyType))
        half = len(candyType) // 2

        return min(unique, half)