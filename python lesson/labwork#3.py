print('Лабораторная работа #3')
for i in range(10):
    if i % 2 == 0:
        print("Четное число:", i)
    else:
        print("Нечетное число:", i)

print(" ")
weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
for i in weekdays:
    print("День", i)

print(" ")
direct_revenue = {83171, 151604, 46315, 98753, 208648, 184682, 204061, 134911, 94791, 109076, 37254, 224991, 149320,
                  83854, 206799, 180922, 235647, 217546, 200478, 239445, 144901, 26522, 177971, 148458, 154937, 196095,
                  140202, 189223}
summa = 0
for element in direct_revenue:
    summa += element

print("Сумма:", summa)

print("")
queriesText = "Cмотреть сериалы онлайн; новости спорта; афиша кино; курс доллара; сериалы этим летом; курс по питону; сериалы про спорт"
print("Количество слов", queriesText.count(" "))

print(" ")
a = int(input("Введите число "))
if a % 2 == 0:
    print("Это четное число")
else:
    print("Это нечетное число")

print(" ")
list_of_strings = ['Москва', 'Новосибирск', 'Воронеж', 'Краснодар', 'Иркутск']
if "Краснодар" in list_of_strings:
    print("Есть")
else:
    print("Нет")
