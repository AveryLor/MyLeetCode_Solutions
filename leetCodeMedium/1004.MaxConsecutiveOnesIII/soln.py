class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0

        for right in range(len(nums)):

            # Flip bits
            if nums[right] == 0:
                k -= 1

            # Enter 1's
            if k < 0: # flipped too many bits
                if nums[left] == 0:
                    k += 1
                left += 1
        
        return right - left + 1

        