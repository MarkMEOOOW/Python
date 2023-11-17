import math


def equationCalculate(a, b, N):
    valuesX = [valueX for valueX in range(1, N)]
    valuesY = [3 * x + a * math.cos(x * b) for x in valuesX]
    return valuesX, valuesY


def quadraticError(yObserved, x, slope, intercept):
    return (yObserved - (slope * x + intercept)) ** 2


a = 3
b = 0.2

N = 25

valuesX, valuesY = equationCalculate(a, b, N)

n = len(valuesX)
sum_x = sum(valuesX)
sum_y_observed = sum(valuesY)
sum_x_squared = sum(x ** 2 for x in valuesX)
sum_xy = sum(x * y for x, y in zip(valuesX, valuesY))

delta = n * sum_x_squared - sum_x ** 2
slope = (n * sum_xy - sum_x * sum_y_observed) / delta
intercept = (sum_x_squared * sum_y_observed - sum_x * sum_xy) / delta

average_quadratic_error = sum(quadraticError(y, x, slope, intercept) for x, y in zip(valuesX, valuesY))

print(f"Func: {slope}x + {intercept}")
print("Average quatrat error:", average_quadratic_error)
