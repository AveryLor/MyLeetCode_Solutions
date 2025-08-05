class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # Convert lists to sets to get unique values
        set1 = set(nums1)
        set2 = set(nums2)

        # Use dictionary to store the difference
        result = {
            "only_in_nums1": [],
            "only_in_nums2": []
        }

        for num in set1:
            if num not in set2:
                result["only_in_nums1"].append(num)

        for num in set2:
            if num not in set1:
                result["only_in_nums2"].append(num)

        return [result["only_in_nums1"], result["only_in_nums2"]]
