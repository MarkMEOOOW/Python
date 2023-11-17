# def check(a, b):
#     for i in range(a, b):
#         if i % 2 != 0:
#             print(i, end=" ")
#
#
# print(check(12, 33))
#
# def check(a: int, b: int) -> list:
#     list1 = []
#     for i in range(min(a, b), max(a, b)):
#         if i % 2 == 1:
#             list1.append(i)
#
#     return list1
#
#
# print(check(12, 32))

# list1 = [random.randint(1, 100) for i in range(10)]
# print(list1)
#
# for i in range(len(list1)):
#     for j in range(len(list1)):
#         if list1[i] < list1[j]:
#             list1[i], list1[j] = list1[j], list1[i]
#
# print(list1)

# a = int(input('Введите число: '))
# abs_number = a if a >= 5 else -a
# print(abs_number)

# try:
#     apples = int(input('Введите число: '))
#     people = int(input('Введите количество людей: '))
#     if apples < 0 or people < 0:
#         raise Exception
#     print(int(apples / people))
#
# except ValueError:
#     print('Введено неверное значение, попробуйте цифры')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except Exception:
#     print('Мы не можем работать с отрицательными числами')

# Что такое API?
# Как производится unit тесты в python

# def foo(number) -> list:
#     spisok = []
#     for i in range(number):
#         if i % 2 == 0:
#             spisok.append(i)
#     return spisok
#
#
# def test() -> None:
#     assert foo(10) == [0, 2, 4, 6, 8]
#     assert foo(3) == [0, 2]
#
#
# test()

# def division(a, b):
#     return max(a, b) / min(a, b)
#
#
# print(division(21, 35))
#
#
# def test():
#     pass


import unittest

# def calculator(expression):
#     allowed = '+-*/'
#
#     if not any(sign in expression for sign in allowed):
#         raise ValueError(f'Выражение должно содержать хотя бы один знак {allowed}')
#     for sign in allowed:
#         if sign in expression:
#             try:
#                 left, right = expression.split(sign)
#                 left, right = int(left), int(right)
#
#                 if sign == "+":
#                     return left + right
#                 elif sign == "-":
#                     return max(left, right) - min(left, right)
#                 elif sign == "*":
#                     return left * right
#                 elif sign == "/":
#                     return max(left, right) / min(left, right)
#             except (ValueError, TypeError):
#                 raise ValueError('Выражение должно содержать 2 целых числа и 1 знак')
#
#
# if __name__ == "__main__":
#     print(calculator("2 + 2"))
