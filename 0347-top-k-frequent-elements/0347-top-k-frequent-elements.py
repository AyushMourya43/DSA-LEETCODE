from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):

        # Har element kitni baar aaya hai, uska count banayenge
        # Example: [1,1,1,2,2,3] → {1:3, 2:2, 3:1}
        freq = Counter(nums)

        # Sabse zyada baar aane wale top k elements nikalenge
        # Example: k=2 → [(1,3), (2,2)]
        # Har tuple mein (number, frequency) hota hai
        most_frequent = freq.most_common(k)

        # Final answer store karne ke liye empty list
        answer = []

        # Har tuple se sirf number chahiye, frequency nahi
        # (1,3) → num=1, count=3
        # (2,2) → num=2, count=2
        for num, count in most_frequent:
            answer.append(num)

        # Top k frequent numbers return kar do
        return answer