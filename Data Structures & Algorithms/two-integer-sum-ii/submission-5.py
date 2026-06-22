class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # l, r = 0, 1

        for l in range(len(numbers)-1):
            for r in range(l, len(numbers)):
                if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
                elif numbers[l] + numbers[r] > target:
                    break

        # l, r = 0, len(numbers) - 1

        # while l < r:
        #     result = numbers[l] + numbers[r]
        #     if result < target:
        #         l += 1
        #     elif result > target:
        #         r -= 1
        #     else:
        #         return [l+1, r+1] 

        return []