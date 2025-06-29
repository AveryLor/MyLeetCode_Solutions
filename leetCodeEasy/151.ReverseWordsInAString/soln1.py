class Solution(object):
    def reverseWords(self, s):
        # Convert string to list to simulate in-place
        chars = list(s)
        
        def reverse(l, r):
            while l < r:
                chars[l], chars[r] = chars[r], chars[l]
                l += 1
                r -= 1
        
        # Step 1: Reverse entire string
        reverse(0, len(chars) - 1)
        
        # Step 2: Reverse each word
        n = len(chars)
        i = 0
        while i < n:
            if chars[i] != ' ':
                start = i
                while i < n and chars[i] != ' ':
                    i += 1
                reverse(start, i - 1)
            else:
                i += 1

        # Step 3: Clean spaces
        result = []
        i = 0
        while i < n:
            if chars[i] != ' ':
                if result and result[-1] != ' ':
                    result.append(' ')
                while i < n and chars[i] != ' ':
                    result.append(chars[i])
                    i += 1
            else:
                i += 1

        return ''.join(result).strip()
