class Solution:
    def productExceptSelf(self, nums):
        
        res = [1] * len(nums)

        # Prefix
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Suffix
        postfix = 1 
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

