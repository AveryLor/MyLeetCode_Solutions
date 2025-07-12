class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Elegant, some might say cute approach (variables are for these three)
        max = -10000
        left = 0
        right = len(height) - 1

        for i in range(len(height)):
            length = right - left
            long = height[left] if (height[left] <= height[right]) else height[right]
            areaUsed = length * long

            # Indexing through, you want to snake 1 by 1 down always taking the tallest
            if (height[left] >= height[right]):
                right -= 1
            else: 
                left += 1

            # Updating to the new max
            if (areaUsed >= max):
                max = areaUsed
        
        return max




        