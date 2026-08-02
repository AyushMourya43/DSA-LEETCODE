class Solution(object):
    def isIsomorphic(self, s, t):
        
         s_to_t = {}
         t_to_s = {}

         for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if c1 in s_to_t:
                 if s_to_t[c1] != c2:
                    return False

            else:
                s_to_t[c1] = c2


           
            if c2 in t_to_s:

                if t_to_s[c2] != c1:
                    return False

            else:
                t_to_s[c2] = c1

         return True

# brute force :

        #  for i in range(len(s)):

        #     # s[i] ka first occurrence
        #     first_s = s.find(s[i])

        #     # t[i] ka first occurrence
        #     first_t = t.find(t[i])

        #     # Agar dono ke first occurrence same nahi
        #     if first_s != first_t:
        #         return False

        #  return True