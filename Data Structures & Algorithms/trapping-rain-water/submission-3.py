class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] # maintain monotonic stack
        result = 0

        for i in range(len(height)):
            entry = None
            while stack and height[stack[-1]] < height[i]:
                mid = stack.pop()
                if stack:
                    h = min(height[i], height[stack[-1]]) - height[mid]
                    w = i - stack[-1] - 1
                    result += h * w

            stack.append(i)
        
        return result