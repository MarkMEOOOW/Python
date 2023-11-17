# import unittest
# import new
#
#
# class TestCalculator(unittest.TestCase):
#
#     def test_addition(self):
#         self.assertEqual(new.addition(2, 2), 4)
#
#     def test_subtraction(self):
#         self.assertEqual(new.subtraction(12, 43), 31)
#
#         with self.assertRaises(ValueError):
#             new.division(2, 0)
#
#
# if __name__ == "__main__":
#     unittest.main()

import numpy as np

arr = np.array([2, 3, 5, 6, 1, 2, 4])

print('Задание #1')
print('Get a new array with elements greater than 3')
arr_gt_3 = arr[arr > 3]
print(f"Array with elements greater than 3: {arr_gt_3}")

print()
print('Задание #2')
print('Get a new array with squared elements')
arr_squared = arr ** 2
print(f"Array with squared elements: {arr_squared}")

print()
print('Задание #3')
print('Get a new array with elements greater than average value')
arr_avg = np.mean(arr)
arr_gt_avg = arr[arr > arr_avg]
print(f"Array with elements greater than average value: {arr_gt_avg}")

print()
print('Задание #4')
print('Create an element-wise multiplication/division/addition of two given arrays')
arr2 = np.array([1, 2, 1, 2, 1, 2, 3])
arr_mult = arr * arr2
arr_div = arr / arr2
arr_add = arr + arr2
print(f"Element-wise multiplication: {arr_mult}")
print(f"Element-wise division: {arr_div}")
print(f"Element-wise addition: {arr_add}")
