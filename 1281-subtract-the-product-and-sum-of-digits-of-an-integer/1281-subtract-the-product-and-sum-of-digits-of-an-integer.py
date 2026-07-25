class Solution(object):
    def subtractProductAndSum(self, n):
         product = 1
         sum =0
         for digit in str(n):
            digit = int(digit)
            sum +=digit
            product *=digit

         return product - sum    