#!/bin/bash

make topic_4_3
if [ $? -ne 0 ]; then
    echo "Ошибка компиляции topic_4_3!"
    exit 1
fi

declare -a test_cases=(
    "3 4 1 9 7 8 6 10 12 11 15 14 13 16"
)

declare -a expected_outputs=(
    "Минимальное максимальное значение находится в ячейке [0][1] и равно 9"
)

for ((i=0; i<${#test_cases[@]}; i++)); do
    read -ra inputs <<< ${test_cases[$i]}
    
    n=${inputs[0]}
    m=${inputs[1]}
    
    elements=( "${inputs[@]:2}" )
    
    input_string="$n $m\n"
    for j in "${elements[@]}"; do
        input_string+="$j\n"
    done
    
    input_string=${input_string%\\n}
    
    result=$(echo -e "$input_string" | ./topic_4_3)
    
    actual_output=$(echo "$result" | grep -oP 'Минимальное максимальное значение.*')
    
    if [[ "$actual_output" == "${expected_outputs[$i]}" ]]; then
        echo "Тест пройден успешно: ${expected_outputs[$i]}"
    else
        echo "Тест не пройден: ${test_cases[$i]}"
        echo "Ожидаемый результат: ${expected_outputs[$i]}"
        echo "Фактический результат: $actual_output"
    fi
done

rm topic_4_3
