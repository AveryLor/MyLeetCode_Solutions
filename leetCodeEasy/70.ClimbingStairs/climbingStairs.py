class Solution(object):
    def climbStairs(self, n):
        temp = 0 
        pre = 1
        curr = 1

        for i in range(1, n): 
            temp = curr
            curr += pre 
            pre = temp

        return curr



        return count; 
