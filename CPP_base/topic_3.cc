#include <cmath>
#include <iostream>
#include <limits>

// Задание 1.1

double calc_func(double x) {
  const double pi = 3.14159265358979323846;
  return 4 * exp(-0.5 * x) * cos(pi * x);
}

int main() {
  double a, b;
  int n;

  std::cout << "Введите начало интервала a: ";
  while (!(std::cin >> a)) {
    std::cout << "Ошибка ввода данных. Пожалуйста, введите число." << std::endl;
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
  }

  std::cout << "Введите конец интервала b: ";
  while (!(std::cin >> b) || (b < a)) {
    std::cout
        << "Ошибка ввода данных. Пожалуйста, введите число больше числа a."
        << std::endl;
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
  }

  std::cout << "Введите количество точек n: ";
  while (!(std::cin >> n) || (n <= 0)) {
    std::cout
        << "Ошибка ввода данных. Пожалуйста, введите целое положительное число."
        << std::endl;
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
  }

  double step = (b - a) / n;
  double negative_numbers_sum = 0;

  for (int i = 0; i <= n; i++) {
    double dot_result = calc_func(a + i * step);
    if (dot_result < 0) {
      negative_numbers_sum += dot_result;
    }
  }

  std::cout.precision(5);
  std::cout << std::fixed;
  std::cout << "Сумма всех отрицательных значений функции f(x) = "
            << "4*exp(-0.5*x)*cos(π*x) в интервале [" << a << ", " << b
            << "] = " << negative_numbers_sum << std::endl;

  return 0;
}
