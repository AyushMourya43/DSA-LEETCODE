class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        
        paragraph = paragraph.lower()

        # Punctuation remove
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        # words in list 
        words = paragraph.split()

        # Fast lookup ke liye banned list ko set me convert kar do
        banned = set(banned)

        # Frequency store karne ke liye dictionary
        count = {}

        # Har word ki frequency count karo
        for word in words:
            if word not in banned:
                count[word] = count.get(word, 0) + 1

        # Maximum frequency wala word find karo
        ans = ""
        max_count = 0

        for word in count:
            if count[word] > max_count:
                max_count = count[word]
                ans = word

        return ans