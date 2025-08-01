class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        count = 0  # Count of 1s in the current window
        k = 1      # Number of zeros we can "delete"
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                count += 1
            else:
                k -= 1

            while k < 0:
                if nums[left] == 1:
                    count -= 1
                else:
                    k += 1
                left += 1

            # max_len is window size (right - left + 1) minus 1 deleted element
            max_len = max(max_len, count)

        return max_len
