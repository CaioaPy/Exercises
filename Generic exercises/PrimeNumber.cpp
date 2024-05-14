//Write a function that accepts an integer and returns whether it is a prime number or not.
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int value;
    vector<int> checker; 
    cout << "insert the value: " << endl;
    cin >> value;
    for (i = 1; i <= value; i++) {
        int y;
        y = value % i;
        if (y == 0) {
            checker.insert(checker.end(), y)
        }
        else {}
    }
    
}