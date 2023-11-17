import numpy as np

# Генерируем случайные данные
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.rand(100, 1)


# Функция для обучения линейной регрессии
def train_linear_regression(X, y, learning_rate=0.01, epochs=1000):
    m = len(y)
    theta = np.random.randn(2, 1)  # Инициализация параметров случайными значениями

    for epoch in range(epochs):
        # Вычисляем предсказания
        y_pred = X.dot(theta)

        # Вычисляем ошибку
        error = y_pred - y

        # Вычисляем градиент
        gradient = 2 / m * X.T.dot(error)

        # Обновляем параметры
        theta -= learning_rate * gradient

    return theta


# Добавляем столбец с единицами для свободного члена
X_b = np.c_[np.ones((100, 1)), X]

# Обучаем модель
theta = train_linear_regression(X_b, y)

# Выводим обученные параметры
print("Обученные параметры theta:")
print(theta)

# Для предсказания новых значений используем theta
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_pred = X_new_b.dot(theta)
print("Предсказанные значения для X_new:")
print(y_pred)
