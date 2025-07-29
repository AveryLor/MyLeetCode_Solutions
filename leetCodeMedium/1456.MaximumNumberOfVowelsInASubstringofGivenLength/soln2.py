class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel = {'a', 'e', 'i', 'o', 'u'} # Hash set data type

        l = 0
        cnt = 0
        res = 0

        for r in range(len(s)):
            cnt += 1 if s[r] in vowel else 0
            if r - l + 1 > k: # Above first iteration
                cnt -= 1 if s[l] in vowel else 0
                l += 1
            res = max(res, cnt)
        return res