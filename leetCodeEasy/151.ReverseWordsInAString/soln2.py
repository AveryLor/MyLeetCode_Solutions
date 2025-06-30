import collections

class Solution: 
    def reverseWorlds(self, s: str) -> str:
        # Split the string into words, filter out empty strings
        string_builder = collections.deque()

        start = -1
        i = 0

        while i < len(s): 
            if s[i] != " ":

                while i < len(s) and s[i] != " ":
                    i += 1
                
                string_builder.appendleft(s[start: i])
                i -= 1
            i += 1

        return " ".join(string_builder).strip() if string_builder else ""
    

# T: O(N)
# S: O(N)