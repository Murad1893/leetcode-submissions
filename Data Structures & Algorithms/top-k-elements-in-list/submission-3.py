from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # x = Counter(nums)
        # sorted_x = sorted(x, key=lambda k: -x[k])
        # return list(sorted_x[:k])

        # bucket sort - variation to use freq as bucket
        buckets = {key: list() for key in range(len(nums)+1)}
        freq_nums = Counter(nums)
        print(buckets)
        for key, value in freq_nums.items():
            buckets[value].append(key)

        result = []
        for i in range(len(buckets)-1, -1, -1):
            result.extend(buckets[i])
            if len(result) == k:
                return result
        
        return result