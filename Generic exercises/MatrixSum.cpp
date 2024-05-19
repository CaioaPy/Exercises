//Write a function that takes two 3x3 matrices and returns their sum as a new 3x3 matrix.
#include <iostream>

using namespace std;

int main() {
    int A [3][3] = {   {5, 1, 2},
                       {7, 8, 3},
                       {8, 3, 6}
                };
    int B [3][3] = {   {8, 6, 1},
                       {9, 2, 7},
                       {3, 4, 5}
                };
    int Sum [3][3];
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++) {
            Sum[i][j] = A[i][j] + B[i][j];
        }
    }
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++) {
            cout << Sum[i][j] << " "; 
        }cout << endl;
    }
}