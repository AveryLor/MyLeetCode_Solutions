class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        temp = n
        for i in range(1, len(flowerbed)-1): 
            if temp == 0: 
                break
            if (flowerbed[i-1] == 0 and flowerbed[i] == 0 and i-1 == 0): 
                flowerbed[i-1] == 1
                temp-=1
            elif (flowerbed[i + 1] == 0 and flowerbed[i] == 0 and i == len(flowerbed)-2):
                flowerbed[i + 1] == 1
                temp-=1
            elif ((flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] != 1)): 
                flowerbed[i] = 1 # Insert a 1
                temp-=1
            
        
        if len(flowerbed) == 1 and flowerbed[0] == 0: 
            temp-= 1

        if len(flowerbed) == 2 and flowerbed[0] == 0 and flowerbed[1] == 0: 
            temp-= 1
        
        if (len(flowerbed) == 3 and flowerbed[0] == 0 and flowerbed[1] == 0 and flowerbed[2] == 0): 
            return True

        return temp <= 0

"""
What's wrong wtih this approach: 

You are trying to do it test case by test case, but you should be generalizing the behavior of the adjacent elements.
"""