class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = 0
        rightSum = 0

        for i in range(len(nums)):
            leftSum += nums[i]
            rightSum = sum(nums[i:])
            
            if leftSum == rightSum:
                return i
        return -1

        