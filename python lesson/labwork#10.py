print('Задание #1')
main_list = [4, -5, -3, -2, 0, 10, -4, 7, 1]

first_list = [i for i in main_list if i > 0 and i % 2 != 0]
print(f'Положительные нечетные числа : {first_list}')

second_list = [abs(i) for i in main_list]
print(f'Преобразовать все элементы в положительные числа: {second_list}')

third_list = int(len([i for i in main_list if i > 0 and i % 2 != 0]))
print(f'Количество положительных нечетных чисел {third_list}')

fourth_list = int(sum([i for i in main_list]) / len(main_list))
print(f'Среднее число {fourth_list}')

fifth_list = int((sum([i for i in main_list if i > 0])) / len(main_list) / (
    sum([i for i in main_list if i < 0])) / len(main_list))
print(f'Среднее количество положительных / отрицательных fifth_list')

sixth_list = [0 if i < 0 else i for i in main_list]
print(f'Замена всех отрицательных чисел на ноль {sixth_list}')

print()
print('Задания #2')

a = int(input('Введите число: '))
list1 = sum([i for i in range(a)])
print(list1)

print()
print('Задание #3')


def fibonacci_number(number):
    fibonacci_numbers = [0, 1]
    fibonacci_numbers.extend(sum(fibonacci_numbers[-2:]) for i in range(2, number))
    print(fibonacci_numbers)


fibonacci_number(12)
