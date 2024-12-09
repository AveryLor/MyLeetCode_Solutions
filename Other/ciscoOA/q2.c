// Essentially just a question to find the solution to the largest palindromic substring



#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// Function to check if a string is a palindrome
bool isPalindrome(const char *str, int start, int end) {
    while (start < end) {
        if (str[start] != str[end]) {
            return false;
        }
        start++;
        end--;
    }
    return true;
}

// Function to find the largest palindromic substring
void funcSubstring(char *inputStr) {
    int length = strlen(inputStr);
    char result[1001] = "None"; // Placeholder for the result
    int maxLength = 0;

    // Iterate over all substrings
    for (int i = 0; i < length; i++) {
        for (int j = i + 1; j < length; j++) { // Substrings of length > 1
            if (isPalindrome(inputStr, i, j)) {
                int subLength = j - i + 1;
                if (subLength > maxLength || 
                   (subLength == maxLength && strncmp(inputStr + i, result, subLength) < 0)) {
                    maxLength = subLength;
                    strncpy(result, inputStr + i, subLength);
                    result[subLength] = '\0'; // Null-terminate the substring
                }
            }
        }
    }

    // Print the result
    printf("%s\n", result);
}

int main() {
    char inputStr[1001];

    // Input the string
    scanf("%s", inputStr);

    // Find the largest palindromic substring
    funcSubstring(inputStr);

    return 0;
}
