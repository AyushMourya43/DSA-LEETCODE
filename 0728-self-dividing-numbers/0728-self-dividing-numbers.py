class Solution(object):
    def selfDividingNumbers(self, left, right):

        ans = []

        for num in range(left, right + 1):
            temp = num
            valid = True

            while temp > 0:  # check all digits
                digit = temp % 10   # last digit

                if digit == 0 or num % digit != 0:   # invalid digit
                    valid = False
                    break

                temp = temp // 10   # remove last digit

            if valid:
                ans.append(num)

        return ans