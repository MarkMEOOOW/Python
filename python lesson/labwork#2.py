print('Задание #1')
astana_users = 4900
astana_revenue = 63000
ARPU1 = astana_revenue / astana_users
print('Astana ARPU is ' + str(ARPU1))

almaty_users = 3500
almaty_revenue = 48000
ARPU2 = almaty_revenue / almaty_users
print('Almaty ARPU is ' + str(ARPU2))

print('')
print('Задание #2')


def plus_one(a):
    return a + 1


def minus_twenty(a):
    return a - 20


def multiplication(a):
    return (a + 1) * 2


def division(a):
    return (a + 5) / 3


def exponentiation(a):
    return (a + 1) ** 5


print(plus_one(1))
print(minus_twenty(24))
print(multiplication(1))
print(division(4))
print(exponentiation(2))

print('')
print("Задание #3")
users_astana = 4900
revenue_astana = 63000

users_almaty = 3500
revenue_almaty = 48000

total_revenue = revenue_almaty + revenue_astana

print('Total revenue is ' + str(total_revenue))

print('')
print('Задание #4')
print('Astana: {} users, revenue {} tenge, ARPU {:.2f}'.format(users_astana, revenue_astana, ARPU1))

print('')
print('Задание #5')
print(float(ARPU1) / float(ARPU2))
print(ARPU2 - ARPU1)
print(ARPU1 > ARPU2)

list = ['one', 434, True]
list.append(242)
print(list)
print(len(list))

listOfNumber = [23, 12, 454, 232]
print(sorted(listOfNumber))

queries_string = 'watch TV series'
print(queries_string.split())

sequence = ['Google Adwords', 'Yandex Direct']
print(sequence[1])

array = ['I am ', 'watching ', 'TV']
array0fWord = ''.join(array)
print(array0fWord)
