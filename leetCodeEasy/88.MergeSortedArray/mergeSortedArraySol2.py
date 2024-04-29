class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]
        
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]

        return nums1