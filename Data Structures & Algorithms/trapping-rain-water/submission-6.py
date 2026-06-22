class Solution:
    def trap(self, height: List[int]) -> int:
        # left right pointer O(1) space

        l, r = 0, len(height) - 1
        max_left = height[l]
        max_right = height[r]

        result = 0
        # intuition: we don't need R or L depending on the increment 
        # since we update based on the min check only
        l += 1
        r -= 1

        while l <= r:
            if max_left <= max_right:
                h = max_left - height[l]
                result = result + h if h > 0 else result
                max_left = max(max_left, height[l])
                l += 1
            else:
                h = max_right - height[r]
                result = result + h if h > 0 else result
                max_right = max(max_right, height[r])
                r -= 1
    
        return result
                
