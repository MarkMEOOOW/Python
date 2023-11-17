def bisection_method(f, a, b, tol=1e-3, max_iter=100):
    """
    Решает нелинейное алгебраическое уравнение f(x) = 0 методом дихотомии (бисекции).
    Параметры:
    - f: Функция, уравнение которой мы хотим решить.
    - a: Левый конец начального интервала.
    - b: Правый конец начального интервала.
    - tol: Допустимая погрешность (по умолчанию 1e-6).
    - max_iter: Максимальное количество итераций (по умолчанию 100).

    Возвращает:
    - x: Приближенное решение уравнения f(x) = 0.
    - iter_count: Количество итераций, затраченных на решение.
    """

    if f(a) * f(b) >= 0:
        print("Метод бисекции не может быть применен. Исходный интервал должен содержать корень.")
        return None

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            print(f"Уравнение решено с точностью {tol} после {iter_count} итераций.")
            return c, iter_count
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    x = (a + b) / 2
    print(f"Уравнение решено с точностью {tol} после {iter_count} итераций.")
    return x, iter_count


# Пример использования:
if __name__ == "__main__":
    # Пример: Решение уравнения x^2 - 4 = 0 на интервале [0, 3]
    f = lambda x: x ** 2 - 4
    a = 0
    b = 3

    solution, iterations = bisection_method(f, a, b)
    if solution is not None:
        print(f"Приближенное решение: x = {solution}")
        print(f"Количество итераций: {iterations}")
