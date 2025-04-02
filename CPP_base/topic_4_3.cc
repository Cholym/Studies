#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main() {
  int n, m;
  cout << "Введите размеры массива (n × m): ";
  cin >> n >> m;

  cout << "Введите значения массива:" << endl;
  int a[n][m], max_in_rows[n], min;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> a[i][j];
      // если это первый элемент, делаем его максимальным
      if (i == 0 && j == 0) max_in_rows[i] = a[i][j];
      // переназначаем максимальное число в этой строке
      else if (a[i][j] > max_in_rows[i])
        max_in_rows[i] = a[i][j];
    }
    if (i == 0) min = max_in_rows[i];
    // ищем минимальное число в этой строке
    else if (max_in_rows[i] < min)
      min = max_in_rows[i];
  }

  int row_index, col_index;
  // ищем расположение минимального элемента в массиве
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (a[i][j] == min) {
        row_index = i;
        col_index = j;
        break;
      }
    }
  }

  cout << "Минимальное максимальное значение находится в ячейке [" << row_index
       << "][" << col_index << "] и равно " << min << endl;

  return 0;
}
