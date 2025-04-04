#include <cstring>
#include <fstream>
#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::fstream;
using std::ios;

// Задание 4.2

struct Car {
  char model[50];
  double rental_day_price;
  double insurance_price;
};

void add_car(fstream &file);
void find_car(fstream &file);

int main() {
  fstream file("cars.dat", ios::in | ios::out | ios::app | ios::binary);

  if (!file.is_open()) {
    cout << "Ошибка открытия файла cars.dat" << endl;
    return 1;
  }

  int choice = 0;
  while (choice != 3) {
    cout << "\nМеню:" << endl;
    cout << "1. Добавить машину" << endl;
    cout << "2. Найти машину" << endl;
    cout << "3. Выйти" << endl;
    cout << "Ваш выбор: ";

    cin >> choice;
    cin.ignore(32767, '\n');
    switch (choice) {
      case 1:
        add_car(file);
        break;
      case 2:
        find_car(file);
        break;
      case 3:
        break;
      default:
        cout << "Ошибка: неверный выбор." << endl;
    }
  }
  file.close();

  return 0;
}

void add_car(fstream &file) {
  Car car;

  cout << "Введите модель автомобиля: ";
  cin.getline(car.model, sizeof(car.model));

  cout << "Введите стоимость проката за день: ";
  cin >> car.rental_day_price;

  cout << "Введите страховую стоимость: ";
  cin >> car.insurance_price;

  file.write(reinterpret_cast<char *>(&car), sizeof(Car));
}

void find_car(fstream &file) {
  char model[50];
  bool found = false;
  cout << "Введите модель автомобиля, которую хотите найти: ";
  cin.getline(model, sizeof(model));

  Car car;
  file.clear();
  file.seekg(0, ios::beg);

  while (file.read(reinterpret_cast<char *>(&car), sizeof(Car))) {
    if (strcmp(car.model, model) == 0) {
      cout << "Автомобиль найден. Страховая стоимость: " << car.insurance_price
           << endl;
      found = true;
      break;
    }
  }

  if (!found) cout << "Автомобиль не найден." << endl;
}
