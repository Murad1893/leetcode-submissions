from itertools import accumulate
from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # division
        # for reduce, given initializer 1 so if all 0s it doesn't crash
        total_prod = reduce(lambda x, y: x*y, filter(None, nums), 1)

        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            return [total_prod if n == 0 else 0 for n in nums]
        else:
            return [total_prod // n for n in nums]


        num_len = len(nums)
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i-1]
            
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                suffix[i] = nums[i]
            else:
                suffix[i] = nums[i] * suffix[i+1]

        # use accumulate
        # prefix = list(accumulate(nums, lambda before, after: before * after))
        # suffix = list(accumulate(reversed(nums), lambda before, after: before * after))[::-1]
    
        for i in range(len(prefix)):
            p = 1 if i == 0 else prefix[i-1]
            s = 1 if i == len(suffix) - 1 else suffix[i+1]

            nums[i] = p * s

        return nums
