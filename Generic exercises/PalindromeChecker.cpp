// Write a C++ program that takes a string input from the user and checks if the string is a palindrome. Ignore spaces, punctuation, and case.

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string str1;
    cout << "insert the string: " << endl;
    cin >> str1;
    string str2 = str1;
    reverse(str2.begin(), str2.end());
    cout << str2 << endl;

}