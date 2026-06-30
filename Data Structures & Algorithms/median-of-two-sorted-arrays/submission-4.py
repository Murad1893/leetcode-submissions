class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # two pointer O(N) pass sol
        # reach half and pick element that is lesser - can be done on O(1) space
        m, n = len(nums1), len(nums2)
        i = j = 0 # pointer to track num 1 and num 2 transitions
        median1 = median2 = 0 # need to move adjacent hence assignment needed

        for c in range((m + n) // 2 + 1):
            median2 = median1 # to ensure they are m -> m + 1
            if i < m and j < n:
                if nums1[i] <= nums2[j]:
                    median1 = nums1[i] 
                    i += 1
                else: 
                    median1 = nums2[j]
                    j += 1
            elif i < m:
                median1 = nums1[i] 
                i += 1
            else: 
                median1 = nums2[j]
                j += 1

        if (m + n) % 2:
            return median1
        else:
            return (median1 + median2)/2
