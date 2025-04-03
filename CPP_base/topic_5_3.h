#include <iostream>

// Задание 3.2

#define MAX_SIZE 1024

using std::cin;
using std::cout;
using std::endl;

int input_array_size(int *n, int *m);
void input_array(int **a, int n, int m);
void define_min_col(int **a, int n, int m, int *min_col);
void rm_min_col(int **a, int **result, int n, int m, int min_col);
void print_array(int **result, int n, int m);
void mem_free(int **a, int n);