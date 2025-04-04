#include <iostream>
#include <fstream>
#include <string>

// Задание 4.1

using std::cin;
using std::cout;
using std::endl;
using std::ofstream;
using std::ifstream;

int main() {
  ofstream ofs("ofs.dat");

  if (!ofs.is_open()) {
    cout << "Ошибка открытия файла ofs.dat";
    return 1;
  }

  double d;

  // Запись в файл
  char choice = 'y';
  while (choice == 'y' || choice == 'Y') {
    bool is_valid = false;
    do {
      cout << "Введите число: ";
      if (!(cin >> d)) {
        cout << "Ошибка ввода. Пожалуйста, введите число." << endl;
        cin.clear();
        cin.ignore(32767, '\n');
      } else
        is_valid = true;
    } while (!is_valid);
    
    ofs << d << endl;
    cout << "Продолжить ввод (y/n)? ";
    cin >> choice;
  }
  ofs.close();
  
  // Чтение из файла
  ifstream ifs("ofs.dat");
  if (!ifs.is_open()){
    cout << "Ошибка открытия файла ofs.dat";
    return 1;
  }
  double product = 1.0;
  while (ifs >> d)
    product *= d;
  
  cout << "Произведение чисел из файла: " << product << endl;
  ifs.close();

  remove("ofs.dat");
  
  return 0;
}
