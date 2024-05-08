//Create a program that converts temperature from Celsius to Fahrenheit and vice versa.
//My code:
#include <iostream>
#include <math.h>

using namespace std;

int main() {
    const char Celsius = 'C';
    const char Fahrenheit = 'F';
    char decision;
    int start_temperature, end_temperature;
    cout << "do you wanna convert C(Celsius -> Fahrenheit) or F(Fahrenheit -> Celsius)?" << endl;
    cin >> decision;
    cout << decision;
    if (decision == Celsius){
        cout << "enter the temperature in Celsius: "<< endl;
        cin >> start_temperature;
        end_temperature = (start_temperature - 32) * 5 / 9;
        cout << "the temperature in Fahrenheit is : " << end_temperature;
    }
    else if (decision == Fahrenheit){
        cout << "enter the temperature in Fahrenheit: "<< endl;
        cin >> start_temperature;
        end_temperature = (start_temperature * 9 / 5) + 32;
        cout << "the temperature in Celsius is : " << end_temperature;
    }
}
