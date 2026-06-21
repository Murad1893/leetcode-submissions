class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            # identify start of sequence
            if n - 1 not in num_set:
                seq = 1
                num = n
                while num + 1 in num_set:
                    seq += 1
                    num += 1
                longest = max(longest, seq)
        
        return longest