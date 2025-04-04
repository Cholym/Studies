#!/bin/bash

clear

make topic_7_1
if [ $? -ne 0 ]; then
    echo "Ошибка компиляции topic_7_1!"
    exit 1
fi

echo "Запускаем программу..."
output=$(./topic_7_1 <<EOF
 6.1
 y
 -2
 y
 8.4
 n
EOF
)

product=$(echo "$output" | grep "Произведение" | awk '{print $NF}')
expected_product=-102.48

if [ "$product" != "$expected_product" ]; then
  echo "Тест провалился! Произведение должно быть $expected_product, но получилось $product."
else
  echo "Тест успешно пройден! Произведение равно $expected_product."
fi

rm -f topic_7_1
