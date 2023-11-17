user_ids = []
with open('user_ids.txt', 'r') as file:
    for line in file:
        user_id = line.strip()
        user_ids.append(user_id)
print(user_ids[0:5], user_ids[-1])
print('lenght of the list =', len(user_ids))
user_ids_set = set(user_ids)
print(f'lent of the unique ids {len(user_ids_set)}')

with open('user_ids_header.txt', 'r') as file:
    print(file.readline())

with open('data_3_columns.txt', 'r') as file:
    lines = file.readlines()
    line = lines[-1].strip().split('\t')
    medium = line[0]
    source = line[1]
    amount = float(line[2].replace(',', '.'))
    print(source, medium, amount, f'| The type of amount = {type(amount)}')

with open('data_3_columns.txt', 'r') as file:
    total_sum = 0
    for line in file:
        line = line.strip().split('\t')
        total_sum += float(line[2].replace(',', '.'))
    print(total_sum)

with open('data_3_columns.txt', 'r') as file:
    total_sum = 0
    for line in file:
        line = line.strip().split('\t')
        if line[0] == 'seo' and line[1] == 'yandex':
            total_sum += float(line[2].replace(',', '.'))
            print(f'Current expense {line[1]} and medium {line[0]} : {total_sum:.2f}')
