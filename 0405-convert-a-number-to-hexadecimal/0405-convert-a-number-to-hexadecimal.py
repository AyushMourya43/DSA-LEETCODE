class Solution(object):
    def toHex(self, num):

        if num == 0:
            return "0"

        num = num & 0xffffffff

        result = ""

        while num > 0:
            remainder = num % 16

            if remainder < 10:
                result += str(remainder)
            else:
                result += chr(ord('a') + remainder - 10)

            num //= 16

        return result[::-1]
