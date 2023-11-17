import math


def celsius(farenheit):
    return f"Celcius is {(5 / 9) * (farenheit - 32)}"


def diameter(radius):
    return f"Diameter is {radius * 2}"


def circumference(radius):
    return f"Circumference is {2 * math.pi * radius}"


def area(radius):
    return f"Area is {math.pi * radius * radius}"


def distance(x1, x2, y1, y2):
    return f"Distance is {math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)}"


def convert(a):
    hour = int(a / 3600)
    minute = int((a % 3600) / 60)
    seconds = a % 60
    return f"Hour is {hour}, minute is {minute}, seconds is {seconds}"


def calculate_change(amount_inserted, price):
    change = amount_inserted - price

    change_dictionary = {50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    for denomination in change_dictionary:
        change_dictionary[denomination] = change // denomination
        change %= denomination

    return change_dictionary


amount_inserted = int(input("Enter the amount inserted: "))
price = int(input("Enter the cost of the item: "))

change_dict = calculate_change(amount_inserted, price)

for denomination, count in change_dict.items():
    if count > 0:
        print(f"Number of {denomination} cent coins: {count}")

print(celsius(12))
print(diameter(12))
print(circumference(12))
print(area(12))
print(distance(12, 32, 12, 32))
print(convert(5049))
calculate_change(75, 20)
