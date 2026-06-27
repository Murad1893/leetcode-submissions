class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # brute force - merge - sort - media

        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) % 2 == 0:
            mid = len(nums1) // 2 - 1
            return (nums1[mid] + nums1[mid+1]) / 2

        return nums1[len(nums1) // 2]