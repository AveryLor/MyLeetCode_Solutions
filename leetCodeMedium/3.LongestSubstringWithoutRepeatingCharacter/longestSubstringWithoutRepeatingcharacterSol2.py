class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        ans = 0

        for cur in arr: 
            if cur not in arr: 
                arr.append(cur)
                ans = max(ans, len(arr)) # The max length between the last answer (last substring, and the current)
            else: 
                for j in range(arr.index(cur)+1): # This effectively resets the array and allows it  
                    arr.pop(0) # To set back up after finding something that was just in the array
                arr.append(cur)
            return ans 