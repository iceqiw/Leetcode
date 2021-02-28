from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        merge = sorted(nums1 + nums2)
        mloc = (n + m) / 2
        loc = int(mloc)
        if loc != mloc:
            loc = mloc - 0.5
            if len(merge) != 0:
                return merge[int(loc)]
            return []
        else:
            v = merge[int(mloc)] + merge[int(mloc - 1)]
            return v / 2
