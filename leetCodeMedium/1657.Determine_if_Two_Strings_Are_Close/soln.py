class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # Condition 1: Must have same set of characters
        if set(word1) != set(word2):
            return False

        # Condition 2: Must have same frequency distribution (ignoring which letter)
        freq1 = sorted(Counter(word1).values())
        freq2 = sorted(Counter(word2).values())

        return freq1 == freq2
            