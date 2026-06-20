from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # x = Counter(nums)
        # sorted_x = sorted(x, key=lambda k: -x[k])
        # return list(sorted_x[:k])

        # bucket sort variation
        freq_x = Counter(nums)
        buckets = {k: [] for k in range(len(nums)+1)}

        for key, value in freq_x.items():
            buckets[value].append(key)

        result = []
        for i in range(len(buckets)-1, -1 , -1):
            result.extend(buckets[i])
            if len(result) == k: return result