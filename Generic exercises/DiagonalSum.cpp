//Write a function to calculate the sum of the primary diagonal elements of a 3x3 matrix.
#include <iostream>

using namespace std;

int main() {
    int Matrix[3][3] = {    {1, 2, 3},
                            {4, 5, 6},
                            {7, 8, 9}
                    };
    int sum;
    for (int i = 0; i < 3; i++) {
        sum += Matrix[i][i];
    }
    cout << sum << endl;
}