class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        np1 = m - 1
        np2 = n - 1
        wp = m + n - 1

        while wp >= 0:
            if np1 < 0:
                nums1[wp] = nums2[np2]
                wp -= 1
                np2 -= 1
            elif np2 < 0:
                nums1[wp] = nums1[np1]
                wp -= 1
                np1 -= 1
            elif nums1[np1] > nums2[np2]:
                nums1[wp] = nums1[np1]
                wp -= 1
                np1 -= 1
            else:
                nums1[wp] = nums2[np2]
                wp -= 1
                np2 -= 1

