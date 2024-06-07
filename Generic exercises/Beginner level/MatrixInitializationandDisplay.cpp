//Create a 3x3 integer matrix. Initialize it with values from 1 to 9. Write a function to display the matrix.
#include <iostream>

using namespace std;

int main() {
    int Lista[3][3] = { {1, 2, 3},
                        {4, 5, 6},
                        {7, 8, 9}
                    };
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            cout << Lista[i][j] << " ";
        }
        cout << endl;
    }
}