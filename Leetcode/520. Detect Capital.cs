//We define the usage of capitals in a word to be right when one of the following cases holds:
//All letters in this word are capitals, like "USA".
//All letters in this word are not capitals, like "leetcode".
//Only the first letter in this word is capital, like "Google".
//Given a string word, return true if the usage of capitals in it is right.

//Example 1:
//Input: word = "USA"
//Output: true

//Example 2:
//Input: word = "FlaG"
//Output: false

//Constraints:
//1 <= word.length <= 100
//word consists of lowercase and uppercase English letters.

public class Solution {
    public bool DetectCapitalUse(string word) {
        int upper = 0;
        int lower = 0;

        foreach (char c in word) {
            if (c >= 'A' && c <= 'Z') {
                upper++;
            } else {
                lower++;
            }
        }

        if ((upper >= 2 && lower >= 1) || (upper == 1 && !(word[0] >= 'A' && word[0] <= 'Z'))) {
            return false;
        } else {
            return true;
        }
    }
}
