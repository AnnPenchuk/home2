N=int(input('Количество палок'))
K=int(input('Количество бросков'))


row = ['I'] * N

for i in range(K):
    query = 'бросок ' + str(i + 1) + ' сбиты палки с номера '
    while True:
        start = int(input(query)) - 1
        if (start >= 0) and (start <= N):
            break
    while True:
        end = int(input('по номер ')) - 1
        if (end >= start) and (end <= N):
            break
    for j in range(start, end + 1):
        row[j] = '.'

print('Результат: ', *row, sep='')