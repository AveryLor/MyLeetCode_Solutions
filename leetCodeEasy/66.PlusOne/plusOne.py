class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        builder=""
        for i in range(len(digits)):
            builder += str(digits[i])
        
        newtotal = str(int(builder) + 1)
        lst = []
        for i in range(len(newtotal)): 
            lst.append(int(newtotal[i]))

        return lst