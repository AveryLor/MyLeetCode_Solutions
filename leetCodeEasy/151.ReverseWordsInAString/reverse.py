# Code for reversing a string

#!/usr/bin/env python3

import sys

def reverseWord(strToReverse):
    strList = list(strToReverse)
    left = 0
    right = len(strToReverse) - 1
    while (left < right): 
        temp = strList[left]
        strList[left] = strList[right]
        strList[right] = temp
        left += 1
        right -= 1
    return ''.join(strList)  # Convert list back to string

    


def main():
    # Your program logic goes here
    strToReverse = "Hello World!"
    print("This is the reversed string: " + reverseWord(strToReverse))

if __name__ == "__main__":
    main()
