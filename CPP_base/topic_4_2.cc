#include <algorithm>
#include <iostream>
#include <random>
#include <vector>

// Задание 2.1

using std::vector;

double max_sum(const vector<double>& arr) {
  double res = 0.0;
  size_t mid = arr.size() / 2;

  for (size_t i = 0; i <= mid; i++) {
    res = std::max(res, arr[i] + arr[arr.size() - i - 1]);
  }
  return res;
}

int main() {
  srand(time(nullptr));
  const size_t N = 10;
  vector<double> array(N);
  for (size_t i = 0; i < N; i++) array[i] = rand() % 100;

  std::cout << "Массив: ";
  for (auto x : array) std::cout << x << ' ';
  std::cout << std::endl;

  std::cout << "Максимальная сумма пар: " << max_sum(array) << std::endl
            << std::endl;
  return 0;
}