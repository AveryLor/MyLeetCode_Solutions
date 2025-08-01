class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        k = 1  # We can delete at most one zero
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            # Update max_len (subtract 1 because we must delete one element)
            max_len = max(max_len, right - left)

        return max_len
