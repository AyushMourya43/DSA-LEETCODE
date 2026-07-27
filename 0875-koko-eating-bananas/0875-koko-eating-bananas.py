import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        
        low = 1 
        high = max(piles) # matlab maximum kele in one hour

        while low <= high:

            mid = low +(high - low)//2    #   Assume Koko ki speed = mid bananas/hour
            hours = 0             # Is speed par total kitne hours lagenge
            for pile in piles:
                hours += math.ceil(pile/mid)    # Ek pile ko finish karne me kitne hours lagenge
                

            if hours <= h:    # Agar h hours ke andar finish ho gaya
                high =mid -1  # Aur chhoti speed try karo

            else:       
                low = mid +1  # Speed kam hai, badhao

        return low        # valid speed     


# agr yahi code python m krnaa h toh forula change hogaa ( hours += math.ceil(float(pile) / mid)). k
# python m // use nhi hotaa work nhi krtaa if u want answer in float than use float or multiply by 1.0