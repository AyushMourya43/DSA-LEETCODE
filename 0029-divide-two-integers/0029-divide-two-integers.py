class Solution(object):
    def divide(self, dividend, divisor):
        
         # Answer ka sign decide karo
        negative = (dividend < 0) != (divisor < 0)
        
         # Positive bana do
        dividend = abs(dividend)
        divisor = abs(divisor)

        answer = 0

        while dividend >= divisor:
            temp = divisor
            count = 1

             # Divisor ko double karte jao
            while dividend >= temp + temp:
                temp = temp + temp
                count = count + count
            
             # Itna part dividend se hata do
            dividend = dividend - temp 
            answer = answer + count

         # Sign lagao
        if negative :
            answer = - answer

         # 32-bit range check
        if answer > 2147483647:
            return 2147483647

        if answer < -2147483648:
            return -2147483648
            
        return answer            