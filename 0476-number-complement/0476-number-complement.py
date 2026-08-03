class Solution(object):
    def findComplement(self, num):
        
        binary = bin(num)[2:] # decimal to binary 

        result =""

        for bit in binary:

            if bit == "1":   # flip
                result +="0"

            else:
                result +="1"

        return int(result,2)       # binary is base 2  
                  # convert binary to decimal 

