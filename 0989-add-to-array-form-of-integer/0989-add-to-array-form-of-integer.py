class Solution(object):
    def addToArrayForm(self, num, k):
        
        ans = []

        i = len(num)-1

        while i >=0 or k > 0:

            if i >= 0:
                k +=num[i]  # current digit add karo


            ans.append(k % 10)  # last digit answer me

            k //= 10        # carry
            i-=1

        return ans[::-1]    

