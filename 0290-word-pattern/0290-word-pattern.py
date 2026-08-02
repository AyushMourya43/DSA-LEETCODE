class Solution(object):
    def wordPattern(self, pattern, s):

        # String ko words ki list me convert karo
        words = s.split()

        # Length same honi chahiye
        if len(pattern) != len(words):
            return False

        # Character Word
        char_to_word = {}

        # Word Character
        word_to_char = {}

    
        for i in range(len(pattern)):

            c1 = pattern[i]
            c2 = words[i]

            # Character to Word mapping
            if c1 in char_to_word:

                if char_to_word[c1] != c2:
                    return False

            else:
                char_to_word[c1] = c2


            # Word to Character mapping
            if c2 in word_to_char:

                if word_to_char[c2] != c1:
                    return False

            else:
                word_to_char[c2] = c1

        return True