class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf') # Start at positive infinity (very large number)
        second = float('inf')
        for i in range(len(nums)): 
            if nums[i] <= first: 
                first = nums[i]    
            elif nums[i] <= second: 
                second = nums[i]
            else: 
                return True
        return False



        