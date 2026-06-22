class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        
        for i in range(len(nums)-1):
            
            l, r = i+1, len(nums)-1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1

        return list(result)

        