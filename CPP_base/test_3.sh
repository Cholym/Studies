#!/bin/bash

make topic_3
if [ $? -ne 0 ]; then
    echo "Ошибка компиляции topic_3!"
    exit 1
fi

declare -a test_cases=(
    "-10 10 100"
    "0 20 50"
    "-15 15 200"
)

declare -a expected_outputs=(
    "-1854.92144"
    "-6.24092"
    "-35625.58683"
)

for ((i=0; i<${#test_cases[@]}; i++)); do
    read -ra inputs <<< ${test_cases[$i]}
    
    result=$(./topic_3 <<< "${inputs[*]}")
    actual_result=$(echo "$result" | awk '{print $NF}')
    
    if [ "$actual_result" == "${expected_outputs[$i]}" ]; then
        echo "Тест пройден успешно: ${test_cases[$i]}"
    else
        echo "Тест не пройден: ${test_cases[$i]}"
        echo "Ожидаемый результат: ${expected_outputs[$i]}"
        echo "Фактический результат: $actual_result"
    fi
done

rm topic_3
