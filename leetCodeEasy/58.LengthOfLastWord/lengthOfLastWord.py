class Solution(object):
    def lengthOfLastWord(self, s):
        output = ""
        lastWord = s.split(" ")
        for current in lastWord:
             if current != '':
                output = current
                
        return len(output)