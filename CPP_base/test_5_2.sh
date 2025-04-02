#!/bin/bash

g++ -std=c++17 -Wall -Wextra -pedantic -o topic_5_2 topic_5_2.cc
if [ $? -ne 0 ]; then
    echo "Ошибка компиляции topic_5_2!"
    exit 1
fi

test_input="5 4 14 -5 -7 -1234 -3 36 1894 0"
expected_output="0 0 0 -5 -7 -1234 -3 0 0 0"

output=$(echo "$test_input" | ./topic_5_2)

actual_output=$(echo "$output" | tail -n 1 | tr -d '\n' | xargs)

if [[ "$actual_output" == "$expected_output" ]]; then
    echo "Тест пройден успешно."
    echo "Результат: $actual_output"

else
    echo "Тест не пройден."
    echo "Ожидаемый результат: $expected_output"
    echo "Фактический результат: $actual_output"
fi

rm topic_5_2
