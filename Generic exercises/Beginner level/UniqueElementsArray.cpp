//Create a program that takes a list of numbers and returns a new list with unique elements of the first list.
#include <iostream>

using namespace std;

void UniqueElements(int arr[], int N){
    for (int i = 0; i < N; i++){
        int j;
        for (j = 0; j < i; j++) {
            if (arr[i] == arr[j]) {
                break;
            }
        }
        if (j == i) {
            cout << arr[i] << " ";
        }
    }
}


int main() {
    int lista[] = {1,2,4,2,3,5,1,2,3,6,5};
    int N = sizeof(lista) / sizeof(lista[0]);
    UniqueElements(lista, N);
}