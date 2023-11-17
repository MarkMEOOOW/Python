class Time:
    def __init__(self, seconds=0):
        self.seconds = seconds
        self.minute = 0
        self.hour = 0

    def convert_seconds(self):
        self.minute = self.seconds // 60
        self.hour = self.minute // 60
        self.seconds %= 60
        self.minute %= 60

    def __str__(self):
        def c(x):
            if x < 10:
                return '0' + str(x)
            else:
                return x

        return f"{c(self.hour)}:{c(self.minute)}:{c(self.seconds)}"


t = Time(3205)

t.convert_seconds()

print(t)


# 2

class MyListClass:
    data: list

    def __init__(self, data):
        self.data = data

    def getMax(self):
        return max(self.data)

    def getMin(self):
        return min(self.data)

    def sameNumb(self):
        """Returns a sorted list of duplicate numbers in the data."""

        duplicates = set()
        for number in self.data:
            if self.data.count(number) > 1:
                duplicates.add(number)

        return sorted(duplicates)

    def countNumb(self, numb):
        return self.data.count(numb)

    def sumList(self):
        return sum(self.data)


list1 = [12, 543, 2312, 35453, 332323, 12]
m = MyListClass(list1)

print(m.getMax())

print(m.getMin())

print(m.sameNumb())

print(m.countNumb(12))

print(m.sumList())
