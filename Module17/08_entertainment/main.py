import random

N=int(input('Количество палок'))
K=int(input('Количество бросков'))


row = ['I'] * N

for i in range(K):

    while True:
        start =random.randint(1,N)
        print('бросок ' + str(i + 1)+' сбиты палки с номера ', start)
        if (start >= 0) and (start <= N):
            break
    while True:
        end = random.randint(start+1,N)-1
        print('по номер ',end)
        if (end >= start) and (end <= N):
            break
    for j in range(start, end + 1):
        row[j] = '.'

print('Результат: ', *row, sep='')