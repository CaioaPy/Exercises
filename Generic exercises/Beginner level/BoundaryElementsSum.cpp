//Write a function to calculate the sum of all boundary elements in a 3x3 matrix.
#include <iostream>

using namespace std;

int main() {
    int matrix[3][3] = {    {1, 2, 3},
                            {4, 5, 6},
                            {7, 8, 9}
                        };
    int sum = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (j == 1 && i == 1){
                continue;
            }
            else {
            sum += matrix[i][j];
            }
        }
    }
    cout << sum << endl;
}