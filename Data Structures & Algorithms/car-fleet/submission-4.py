class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Intuition:
        - All cars are on the same road hence cars later ahead cannot be crossed
        - Sorting to start with the latest car first
        - To know if the cars make a fleet, we need to find intersection
            - Cars intersect if the time to reach target of the one behind is lesser than the one in front
        - All cars would be one fleet if they intersect. 
        - If there are multiple fleets, meaning they are arriving at dest at different times
        - So we can maintain a stack to keep track of this. Always compare with the top.
        - Only top is needed, since no matter how fast the car, sorting ensures they stay behind and 
            if the one next to it is still on stack meaning it ensures the faster one can't be the part of the 
            fleet ahead of it 
        """
        def time_to_dest(index):
            return (target - position[index][0]) / position[index][1] 

        stack = []
        for i in range(len(position)):
            position[i] = [position[i], speed[i]]

        position = sorted(position, key=lambda x: x[0]) # sort based on position

        for i in range(len(position)-1,-1,-1):
            if not stack or time_to_dest(i) > time_to_dest(stack[-1]):
                stack.append(i)
        
        return len(stack)
            


        