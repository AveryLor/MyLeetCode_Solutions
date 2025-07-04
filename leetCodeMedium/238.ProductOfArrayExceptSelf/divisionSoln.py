class Solution:
    def productExceptSelf(self, nums):
        product = 1
        for i in range(len(nums)): 
            product *= nums[i]

        for i in range(len(nums)): 
            nums[i] = product / nums[i]

        return nums 
