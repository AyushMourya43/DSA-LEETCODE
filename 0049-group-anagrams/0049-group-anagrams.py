class Solution(object):
    def groupAnagrams(self, strs):
       
      # Empty dictionary banayi
        groups = {}

        # Har word ke liye
        for word in strs:

            # Word ko sort karke string bana di
            key = "".join(sorted(word))

            # Agar key pehle se nahi hai to empty list banao
            if key not in groups:
                groups[key] = []    

            # Word ko us group me add karo
            groups[key].append(word)

        # Sirf groups ki values return kar do
        return list(groups.values())