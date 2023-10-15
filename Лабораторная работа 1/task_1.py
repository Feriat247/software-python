numbers = [2, -93, -2, 8, None, -44, -1, -85, -14,
           90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

# Создание множества исключающее None
numbers_new = numbers[0:4:1] + numbers[5::]
print("Новое множество исключающее None => ", numbers_new)

# Создание суммы, количества множества и подсчет его среднего значения
sum_numbers = sum(numbers_new)
count_numbers = len(numbers_new)
average_numbers = sum_numbers / count_numbers

# Замена элемента None в оригинальном множестве
numbers[4] = round(average_numbers, 2)

print("Сумма множества:", sum_numbers)
print("Количество элементов множества:", count_numbers)
print("Среднее арифметическое множества:", average_numbers)

print("Измененный список:", numbers)
