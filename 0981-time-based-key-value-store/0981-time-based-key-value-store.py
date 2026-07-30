from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        
        self.mp = defaultdict(list)

    def set(self, key, value, timestamp):
        self.mp[key].append((timestamp,value))
        

    def get(self, key, timestamp):
       
        if key not in self.mp:
            return ""

        arr = self.mp[key]

        left = 0
        right = len(arr) - 1    
        # latest valid value
        ans = ""

        while left <= right:

            mid = (left + right) // 2

            # current timestamp valid hai
            if arr[mid][0] <= timestamp:

                # value save karo
                ans = arr[mid][1]

                # aur latest valid timestamp dhoondo
                left = mid + 1

            else:
                # timestamp bada hai, left side jao
                right = mid - 1

        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)