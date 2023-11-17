def linear_interpolation(x, x_list, y_list):
    i = 0
    while i < len(x_list) - 1:
        if x >= x_list[i] and x < x_list[i + 1]:
            break
        i += 1

    if i == len(x_list) - 1:
        return y_list[i]
    else:
        return y_list[i] + (y_list[i + 1] - y_list[i]) / (x_list[i + 1] - x_list[i]) * (x - x_list[i])


def main():
    # Инициализируем массивы данных.
    x_list = [1, 2, 3, 4, 5]
    y_list = [2, 3, 4, 5, 6]

    # Вычисляем значение функции y(x) в точке x = 3.
    x = 3
    y = linear_interpolation(x, x_list, y_list)

    # Выводим результат.
    print("y(x) = ", y)


if __name__ == "__main__":
    main()
