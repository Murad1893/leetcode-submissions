import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = l + (r-l) // 2
            print(matrix[mid][0], matrix[mid][-1])
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                index = bisect.bisect_left(matrix[mid], target)
                return True if index < len(matrix[mid]) and matrix[mid][index] == target else False
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1 

        return False
        