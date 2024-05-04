class Solution(object):
    def longestCommonPrefix(self, strs):
        # Longest common prefix string
        lcp = ""
        # Base condition
        if strs is None or len(strs) == 0:
            return lcp
        # Find the minimum length string from the array
        minimumLength = len(strs[0])

        for i in range(1, len(strs)):
            minimumLength = min(minimumLength, len(strs[i]))

        for i in range(0, minimumLength):
            current = strs[0][i]

            for j in range(1, len(strs)):
                if (current != strs[j][i]):
                    return lcp
            lcp += current

        return lcp