class Solution:
    def findMin(self, nums: List[int]) -> int:
        # intuition is to find the pivot so you know to search in unsorted half
        l, r = 0, len(nums) - 1
        result = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            mid = l + (r-l)//2
            result =min(result, nums[mid])

            # >= required, because for mid == l, we would want to return 
            if nums[mid] <= nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        
        return result
        