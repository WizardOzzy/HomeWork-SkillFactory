# Фукция сортировки
def sorting(b):
    for i in range(1, len(b)):
        x = b[i]
        idx = i
        while idx > 0 and b[idx-1] > x:
            b[idx] = b[idx-1]
            idx -= 1
        b[idx] = x
    print(b)
    return b


# Фукция двоичного поиска
def binary_search(b, element, left, right):
        if left > right:
            return False
        middle = (right + left) // 2
        if b[middle] == element:
            return middle
        elif element < b[middle]:
            return binary_search(b, element, left, middle - 1)
        else:
            return binary_search(b, element, middle + 1, right)


# функция проверки введенных данных на соответствие целым числам
def is_int(str):
    str = str.split()
    for n in str:
        try:
            int(n)
        except ValueError:
            return False
    return True

# Ввод множества чисел и последующие проверки на неккоректность ввода
arr = []
check = False
while not check:
    numbers = input("Введите через пробел последоваетльность чисел которые хотите отсортировать: " )
    if " " not in numbers:
        print("\nВ вводе отсутсвуют пробелы (введите числа, согласно условиям ввода.)")
    elif not is_int(numbers):
        print('\nВ вводе содержатся не цифры либо не целые числа (введите числа, согласно условиям ввода.)\n')
    else:
        arr = list(map(int, numbers.split()))
        check = True

# Ввод искомого числа и последующие проверки на неккоректность ввода
element = " "
check_element = False
while not check_element:
    element = input("Введите цифку индекс которой вы хотите найти: ")
    if not is_int(element):
        print('\nВ вводе содержатся не цифра либо не целое число (введите число, согласно условиям ввода.)\n')
    elif " " in element:
        print('\nВ вводе содежрится больше одной цифры.)\n')
    else:
        element = int(element)
        check_element = True

b = sorting(arr)


# Вывод Результатов Поиска (Искомое число и его индекс или ближайщие числа и их индексы)

min_element = b[0]
max_element = b[len(b) - 1]

if (element >= min_element and element <= max_element):
    try:
        if b.index(element):
            print(f'Индекс введенного элемента: {binary_search(b, element, 0, len(b))}')
    except:
        rI = min(b, key=lambda x: (abs(x - element), x))
        ind = b.index(rI)
        max_ind = ind + 1
        min_ind = ind - 1
        if rI < element:
            print("Число не найдено")
            print(f'Ближайший меньший элемент: {rI}, его индекс: {ind}')
            print(f'Ближайший больший элемент: {b[max_ind]}, его индекс: {max_ind}')
        elif rI > element:
            print("Число не найдено")
            print(f'Ближайший меньший элемент: {b[min_ind]}, его индекс: {min_ind}')
            print(f'Ближайший больший элемент: {rI}, его индекс: {ind}')

elif element < min_element:
    print(f'заданное число меньше минимального числа в массиве, ближайшее большее {min_element}, его индекс: 0')
elif element > max_element:
    print(f'заданное число больше максимального числа в массиве, ближайшее меньшее {max_element}, его индекс: {len(b)-1}')

