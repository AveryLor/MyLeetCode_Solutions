class Solution(object):
    def findMaxAverage(self, nums, k):
        sum = sum(nums[:k])
        max = s
        for i in range(k, len(nums)):
            sum += nums[i] - nums[i - k]
            if sum > max:
                max = sum
        return max / float(k)