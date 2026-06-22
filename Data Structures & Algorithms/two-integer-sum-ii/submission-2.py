class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing order means it's sorted so O(N) pass

        l, r = 0, 1

        for l in range(len(numbers)-1):
            for r in range(l, len(numbers)):
                if numbers[l] + numbers[r] == target:
                    return [l+1, r+1]

        return []