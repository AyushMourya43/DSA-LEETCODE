class Solution(object):
    def countAndSay(self, n):
        
        # Starting string hamesha "1" hoti hai
        s = "1"
        
        for _ in range(n - 1):  # Har baar current string se next string banayenge
                                # "1" se n-th string tak jaane ke liye n-1 baar
            result = ""
            i = 0
            
             # Jab tak poori string read nahi ho jaati
            while i < len(s):
                first_digit = s[i]
                count = 0
                
                 # Jab tak same digit continuously mil raha hai
                while i < len(s) and s[i] == first_digit:
                    count += 1
                    i += 1

                result += str(count) + first_digit

            s = result

        return s