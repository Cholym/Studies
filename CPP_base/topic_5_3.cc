#include "topic_5_3.h"

int main() {
    int n, m;
    if (input_array_size(&n, &m) == 1) return 1;

    int **a = new int*[n];
    input_array(a, n, m);

    int min_col;
    define_min_col(a, n, m, &min_col);

    int **result = new int*[n];

    rm_min_col(a, result, n, m, min_col);
    print_array(result, n, m - 1);

    mem_free(a, n);
    mem_free(result, n);

    return 0;
}

int input_array_size(int *n, int *m) {
    cout << "Введите размер массива, столбцы и строки: ";
    cin >> *n >> *m;

    if (*n <= 0 || *m <= 0 || *n > MAX_SIZE || *m > MAX_SIZE) {
        cout << "Ошибка: размеры массива должны быть положительными и не более " << MAX_SIZE << "." << endl;
        return 1;
    }
    return 0;
}

void input_array(int **a, int n, int m) {
    for (int i = 0; i < n; ++i)
        a[i] = new int[m];
    cout << "Введите значения для массива в " << n << " строк и " << m << " столбцов:" << endl;
    for (int i = 0; i < n; i++) 
        for (int j = 0; j < m; j++) 
            cin >> a[i][j];
}

void define_min_col(int **a, int n, int m, int *min_col) {
    int min = a[0][0];
    *min_col = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] < min) {
                min = a[i][j];
                *min_col = j;
            }
        }
    }
}

void rm_min_col(int **a, int **result, int n, int m, int min_col) {
    for (int i = 0; i < n; ++i)
        result[i] = new int[m - 1]; 
    for (int i = 0; i < n; i++) {
        for (int j = 0, j_1 = 0; j < m; j++) {
            if (j == min_col) {
                continue;
            } else {
                result[i][j_1++] = a[i][j];
            }
        }
    }
}

void print_array(int **result, int n, int m) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            cout << result[i][j] << ' ';
        cout << endl;
    }
}

void mem_free(int **a, int n){
    for (int i = 0; i < n; ++i)
        delete[] a[i];
    delete[] a;
}