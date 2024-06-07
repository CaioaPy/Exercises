//Write a function that takes an array of integers and its size as parameters and returns the average of the elements.
#include <iostream>

using namespace std;

int ArrayAverage(int numbers[], int size) {
    int total = 0;
    int average;
    for (int i = 0; i < size; i++) {
        int x;
        x = numbers[i];
        total += x;
    }
    average = total / size;
    return average;
}

int main() {
    int size, y;
    int listafodahaha[7] = {1, 23, 52, 123, 4, 65, 2};
    size = sizeof(listafodahaha) / sizeof(listafodahaha[0]);
    y = ArrayAverage(listafodahaha, size);
    cout << y << endl;
}