class Solution {
    public String mergeAlternately(String word1, String word2) {
        int totalLetters = word1.length() + word2.length();
        int oneLen = word1.length(); 
        int twoLen = word2.length(); 
        String builder = ""; 
        int counterOne = 0; 
        int counterTwo = 0; 
        int counter = 0; 
    
        while(totalLetters > 0) {
            if ((counter == 0 || counter % 2 == 0 || counterTwo == twoLen) && counterOne != oneLen) { // Word one test case
                builder += word1.charAt(counterOne++); 
            } else if (counterTwo != twoLen) {
                builder += word2.charAt(counterTwo++); 
            }
            totalLetters--; 
            counter++;
        }
        return builder; 
    }
}