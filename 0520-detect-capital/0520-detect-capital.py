class Solution(object):
    def detectCapitalUse(self, word):
        
        return (
            word.isupper() or
            word.islower() or
            word.istitle()
        )


# if word == word.upper():
#             return True

#         if word == word.lower():
#             return True

#         if word == word.capitalize():
#             return True

#         return False