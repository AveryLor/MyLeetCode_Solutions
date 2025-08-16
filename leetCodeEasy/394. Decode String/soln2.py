class Solution(object):
    def decodeString(self, s):
        def decode(i):
            result = ''
            while i < len(s) and s[i] != ']':
                if s[i].isalpha():
                    result += s[i]
                    i += 1
                else:
                    num = 0
                    while s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    i += 1  
                    sub, i = decode(i)
                    i += 1  
                    result += sub * num
            return result, i

        return decode(0)[0]