//Write a function that takes an array of integers and its size as parameters and returns the average of the elements.
#include <iostream>

using namespace std;

int ArrayAvarage(int numbers[], int size) {
    int total = 0;
    int avarage;
    for (int i = 0; i < size; i++) {
        int x;
        x = numbers[i];
        total += x;
    }
    avarage = total / size;
    return avarage;
}

int main() {
    int size, y;
    int listafodahaha[7] = {1, 23, 52, 123, 4, 65, 2};
    size = sizeof(listafodahaha) / sizeof(int);
    y = ArrayAvarage(listafodahaha, size);
    cout << y << endl;
}