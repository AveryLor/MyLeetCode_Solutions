class Solution(object):
    def isPalindrome(self, x):
        str_x = str(x)
        return str_x == str_x[::-1]