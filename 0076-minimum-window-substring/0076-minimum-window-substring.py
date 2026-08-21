from collections import Counter
class Solution(object):
    def minWindow(self, s, t):

        need = Counter(t)
        left = 0
        count = 0
        min_len = float("inf")
        answer = ""

        for right in range(len(s)):
             if s[right] in need:
                 if need[s[right]] > 0:
                     count +=1
                 need[s[right]] -= 1 

             while count == len(t):
                    if right - left + 1 < min_len:
                        min_len = right - left + 1
                        answer = s[left : right + 1]
                    if s[left] in need:
                        need[s[left]] += 1

                        if need[s[left]] > 0:
                            count -= 1
                    left += 1    

        return answer                


# from collections import Counter

# class Solution(object):
#     def minWindow(self, s, t):

#         # t ke characters ki frequency store karo
#         # Example: t = "ABC" → {A:1, B:1, C:1}
#         need = Counter(t)

#         # Window ka starting point
#         left = 0

#         # t ke kitne required characters mil chuke hain
#         count = 0

#         # Abhi tak minimum window nahi mili
#         min_len = float("inf")

#         # Final answer
#         answer = ""

#         # right pointer poori string mein chalega
#         for right in range(len(s)):

#             # Agar current character t mein required hai
#             if s[right] in need:

#                 # Agar ye character abhi required tha
#                 if need[s[right]] > 0:
#                     count += 1

#                 # Ek required character mil gaya
#                 need[s[right]] -= 1

#             # Jab window mein t ke saare characters aa gaye
#             while count == len(t):

#                 # Current window ki length previous minimum se chhoti hai?
#                 if right - left + 1 < min_len:

#                     # Minimum length update karo
#                     min_len = right - left + 1

#                     # Current window ko answer banao
#                     answer = s[left:right + 1]

#                 # Left wala character window se remove kar rahe hain
#                 if s[left] in need:

#                     # Us character ki requirement wapas badhao
#                     need[s[left]] += 1

#                     # Agar requirement > 0 ho gayi
#                     # matlab required character missing ho gaya
#                     if need[s[left]] > 0:
#                         count -= 1

#                 # Window ka left point aage move karo
#                 left += 1

#         # Sabse chhoti valid window return karo
#         return answer
        
        