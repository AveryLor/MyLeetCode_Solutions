class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Initializing variables 
        maximum = 0 
        check = []

        for char in s: #Iterating through the entire string 
            if char in check: #If it is in check 
                idx = check.index(char) #gets its index 
                del check[:idx+1] #Delete all elements up to and including the index from the check list 
            check.append(char) # Append the current character to the check list 
            maximum = max(maximum, len(check)) #Update the maximum length 
        return maximum