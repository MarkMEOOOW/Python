# A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#
# B = [[x ** 2 for x in row] for row in A]
#
# print(B)
# def dictionary(number):
#     word = []
#     for i in range(number):
#         i = int(input(f'Введи {i + 1} число: '))
#         word.append(i)
#     return word
#
#
# print(dictionary(int(input('Введите число: '))))
import random


# a = {i ** 2 for i in range(1, 7)}
# print(a)

# def work(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
#
# res = work(18, 24)
# print(res)
#
#
# def addition(a, b):
#     return a + b
#
#
# def subtraction(a, b):
#     return max(a, b) - min(a, b)
#
#
# def multiplication(a, b):
#     return a * b
#
#
# def division(a, b):
#     if min(a, b) == 0:
#         raise ValueError('--Division by Zero--')
#     return a / b
#
#
# def square_root(a):
#     if a < 0:
#         raise ValueError('--Must be more than 0--')
#     return math.sqrt(2)
#
#
# def power(a, b):
#     if b < 0:
#         raise ValueError('--Not available in basic calculator--')
#     return math.pow(a, b)

# def numbers(*args):
#     summa = 0
#     for i in args:
#         summa += i
#     return summa
#
#
# a = (12, 2435, 2323)
# print(numbers(*a))

# def foo(length: int = 10):
#     result = []
#     for i in range(length):
#         if i % 2 == 0:
#             result.append(i)
#     return result
#
#
# print(foo())

# def print_fibonacci_numbers(number):
#     fibonacci_numbers = [0, 1]
#     for i in range(2, number + 1):
#         fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
#     print(fibonacci_numbers)
#
#
# print(print_fibonacci_numbers(int(input('Введите число: '))))

# def print_fibonacci_numbers(number):
#     fibonacci_numbers = [0, 1]
#     sum_of_last_two_numbers = 0
#     for i in range(2, number):
#         sum_of_last_two_numbers = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
#         fibonacci_numbers.append(sum_of_last_two_numbers)
#
#     print(fibonacci_numbers)
#
#
# print_fibonacci_numbers(10)
# def division(a: int, b: int) -> int:
#     return int(max(a, b) / min(a, b))

class House:
    def __init__(self, street, number):
        self.street = street
        self.number = number

    def build(self):
        print(f'Дом на улице {self.street} под номером {self.number} построен')


Hawaii = House('Abaya', 19)
Hawaii.build()
