print('Лабораторная работа #4')


def replace_tuple(replace_list, replace_value):
    new_list = list()
    for i in replace_list:
        other_list = list(i)
        other_list[-1] = replace_value
        new_list.append(tuple(other_list))
    return new_list


def tuple_mul(thistuple):
    sum = 1
    for i in thistuple:
        sum *= i
        return sum


def average_tuple(thistuple: tuple):
    new_list = list()
    for i in thistuple:
        suma = sum(i) / len(i)
        new_list.append(suma)
    return new_list


def check_tuples(tuple, condValue):
    for i in tuple:
        if condValue in i:
            return f"Check if {condValue} present in said tuple of tuples \nTrue"
    return f"Check if {condValue} present in said tuple of tuples \nFalse"


def concatenate_dicts(dic1: dict, dic2: dict):
    new_dict = dict(dic1)
    new_dict.update(dic2)
    return new_dict


def sum_common_elements(dic1: dict, dic2: dict):
    new_list = list(dic1.keys())
    new_dict = dict()
    for i in new_list:
        if i in dic2.keys():
            new_dict.update({i: (dic1.get(i) + dic2.get(i))})
    return new_dict


def find_max(thiset: set):
    lest = list()
    lest.append(max(thiset))
    lest.append(min(thiset))
    return lest;


def find_length(thiset: set):
    return len(thiset)


def present_val(thiset: set, condVal):
    if condVal in thiset:
        return f"Yes we have {condVal} in the set!!!"
    return f"No, We doesn't have {condVal} in the set((("


this_tuple = (100, 200, 300)
print(format(f"This is tuple {this_tuple}"))
new_list = [(12, 410, 4123, 123), (123, 124, 1200, 13233, 123123), (5235, 23212, 2342)]
new_tuple = ((123, 11, 11, 123), (0, 0, 0, 4), (3, 2, 4))
another_tuple = (("yellow", "white", "black"), ("orange", "lime", "pink"), ("green", "purple", "blue"))
print(replace_tuple(new_list, 100))
print(tuple_mul((4, 3, 2, 2, -1, 18)))
print(average_tuple(new_tuple))
print(check_tuples(another_tuple, "blue"))
val = {0: 10, 1: 20, 2: 30, 3: 40}
val2 = {0: 110, 1: 210, 7: 310, 5: 410}
print(concatenate_dicts(val, val2))
print(sum_common_elements(val, val2))
mSet = {"234", "2341", "0", "12312", "2342341123", "5"}
print(find_max(mSet))
print(find_length(mSet))
print(present_val(mSet, 322))
