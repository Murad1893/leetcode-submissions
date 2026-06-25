class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        pse = [-1] * len(heights)
        nse = [len(heights)] * len(heights)
        stack = []
        result = 0

        # create pse array
        for i in range(len(heights)):
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1][0]
            stack.append([i, heights[i]])

        stack = []
        # create nse array
        for i in range(len(heights)-1,-1,-1):
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1][0]
            stack.append([i, heights[i]])
       
        # compute area using nse - pse 
        for i in range(len(heights)):
            result = max(result, (nse[i] - pse[i] - 1) * heights[i])
        
        return result