# lol 

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Brute force approach
        max = -10000

        for i in range(len(height) - 1): 
            for j in range(i + 1, len(height)): 
                limiter = height[i] if (height[i] <= height[j]) else height[j]
                areaUsed = (j - i) * limiter

                if (areaUsed >= max): 
                    max = areaUsed
        
        return max

        