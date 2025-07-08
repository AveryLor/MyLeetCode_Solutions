class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        i = 0
        idx = 0  # pointer for writing compressed chars in-place

        while i < n:
            currentChar = chars[i]
            count = 0
            while i < n and chars[i] == currentChar:
                count += 1
                i += 1
            
            # Write the character
            chars[idx] = currentChar
            idx += 1
            
            # Write the count (only if > 1)
            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1

        return idx
