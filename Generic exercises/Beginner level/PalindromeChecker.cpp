// Write a C++ program that takes a string input from the user and checks if the string is a palindrome. Ignore spaces, punctuation, and case.

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string str1, str1_formated;
    cout << "insert the string: " << endl;
    getline(cin, str1);
    for (char i : str1){
        if (isalnum(i)){
            str1_formated += tolower(i);
        }
    }

    string str2 = str1_formated;
    reverse(str2.begin(), str2.end());
    cout << str2 << endl;

    bool equal = false;

    if (str1_formated == str2) {
        cout << str1 << " is a palindrome";
    }
    else{
        equal = false;
        cout << str1 << " isn't a palindrome";
    }
    

}