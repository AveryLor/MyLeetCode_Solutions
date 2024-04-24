class Solution:
    def isPalindrome(self, s: str) -> bool:
        strBuilder = ""
        for i in range(len(s)):  
            if ((s[i].lower() >= "a" and s[i] != "}" and s[i] != "{") or s[i].isdigit()  ):
                strBuilder += s[i].lower()
        print(strBuilder)
        
        return (strBuilder == strBuilder[::-1])
