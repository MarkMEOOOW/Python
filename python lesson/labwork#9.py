import math


class myTime:
    def __init__(self, second, minute, hour):
        self.second = second
        self.minute = minute
        self.hour = hour

    def convert_to_seconds(self):
        return self.second + 60 * self.minute + 3600 * self.hour

    def convert_to_minutes(self):
        return self.minute + self.hour * 60


class analogTime(myTime):
    def __init__(self, second, minute, hour):
        super().__init__(second, minute, hour)

    def to_analog_time(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def to_current_time(self):
        while self.hour > 24:
            self.hour -= 24
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def to_american_time(self):
        am_pm = "a.m." if self.hour < 12 else "p.m."
        return f"{self.hour % 12:02}:{self.minute:02}:{self.second:02} {am_pm}"


time = analogTime(12, 34, 11)

seconds = time.convert_to_seconds()
minutes = time.convert_to_minutes()
current = time.to_current_time()

print(seconds)
print(minutes)
print(current)

analog_time = time.to_analog_time()
american_time = time.to_american_time()

print(analog_time)
print(american_time)


# Exercise #2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.radius


circle = Circle(0, 0, 10.0)

area = circle.get_area()
circumference = circle.get_circumference()

print(area)
print(circumference)
