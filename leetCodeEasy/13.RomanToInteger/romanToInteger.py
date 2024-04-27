class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        currentVal = 0
        preVal = 0
        sum = 0

        for i in reversed(s):
            currentVal = map[i]
            if (currentVal >= preVal): 
                sum += currentVal 
            else: 
                sum -= currentVal 
            preVal = currentVal 
        return sum