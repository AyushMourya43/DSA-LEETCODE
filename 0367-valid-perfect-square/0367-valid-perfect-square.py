class Solution(object):
    def isPerfectSquare(self, num):
        
        i = 1
        while i*i <= num:
            if i*i == num:
               return True
            i +=1

        return False   

# import math

# class Solution(object):
#     def isPerfectSquare(self, num):
        
#         if math.isqrt(num) ** 2 == num:
#             return True
#         else:
#             return False



# import math

# class Solution(object):
#     def isPerfectSquare(self, num):
#         return math.isqrt(num) ** 2 == num

