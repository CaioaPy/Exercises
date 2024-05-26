//Write a function to calculate the sum of the primary diagonal elements of a 3x3 matrix.
#include <iostream>

using namespace std;

int main() {
    int Matrix[3][3] = {    {2, 2, 3},
                            {4, 5, 6},
                            {6, 8, 9}
                    };
    int sum;
    for (int i = 0; i < 3; i++) {
        sum += Matrix[i][i];
    }
    cout << "main diagonal: "<< sum << endl;

    int sum2 = 0;
    int o = 0;
    for (int j = 1; j < 4; j++){
            int i = 3 - j;
            cout << o << i << endl;
            sum2 += Matrix[o][i];
            o++;
    }
    cout << "second diagonal: "<< sum2 << endl;
}