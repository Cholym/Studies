#include <iostream>

#define n 10

using std::cin;
using std::cout;
using std::endl;

void input_array(int *arr) {
    cout << "Введите значения для массива в " << n << " элементов:" << endl;
    for (int i = 0; i < n; i++)
        cin >> arr[i];
} 

void positive_to_zero (int *arr) {
  for (int i = 0; i < n; i++)
    arr[i] = arr[i] > 0 ? 0 : arr[i];
}

void print_array(int *arr) {
    cout << "Массив после преобразования:" << endl;
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main() {
  
    int a[n];
    input_array(a);
    positive_to_zero(a);
    print_array(a);

  return 0;
}