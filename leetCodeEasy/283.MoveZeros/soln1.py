class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZero = 0 

        # First pass: move non-zero elements forward
        for i in range(len(nums)): 
            if nums[i] != 0: 
                nums[lastNonZero] = nums[i]
                lastNonZero += 1

        # Second pass fill in the remaining slots with 0's
        for i in range(lastNonZero, len(nums)): 
            nums[i] = 0 # Remaining are zeros

        
        