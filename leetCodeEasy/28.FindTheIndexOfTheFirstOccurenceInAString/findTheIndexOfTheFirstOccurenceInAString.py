class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """


        builder = ""
        for j in range(len(haystack)):
            if (haystack[j] == needle): 
                return j
            
            builder = ""
            builder += haystack[j]
            for i in range(j + 1, len(haystack)):
                builder += haystack[i]
                if (builder == needle): 
                    return j
        
        return -1