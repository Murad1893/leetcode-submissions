class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        def recurse(low, high):
            if low > high:
                return -1
            
            mid = low + (high-low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return recurse(mid+1, high)
            else:
                return recurse(low, mid-1)
        
        return recurse(0, len(nums) - 1)