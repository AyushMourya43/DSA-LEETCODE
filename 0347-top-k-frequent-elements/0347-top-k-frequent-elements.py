from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):

        freq = Counter(nums)

        most_frequent = freq.most_common(k)

        answer = []

        for num, count in most_frequent:
            answer.append(num)

        return answer