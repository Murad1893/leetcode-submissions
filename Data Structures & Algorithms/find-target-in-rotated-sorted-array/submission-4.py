import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l
        l, r = 0, len(nums) - 1

        # identify the range in which it lies
        # the range is 0 ... pivot - 1 | pivot ... end
        # pivot is the minimum hence belongs to the right half so you exclude by pivot - 1
        if nums[pivot] <= target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1

        
        
        