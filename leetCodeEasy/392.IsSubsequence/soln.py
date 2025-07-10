class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        strBuilder = ""
        charTracker = 0
        for i in range(len(t)): 
            if charTracker >= len(s):
                break
            if s[charTracker] == t[i]: 
                strBuilder += t[i]
                charTracker += 1
        
        return strBuilder == s

        