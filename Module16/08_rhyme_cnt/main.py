N=int(input('введите кол-во человек:'))
K=int(input('введите число в считалке:'))

start=0
list1=[]
for i in range(1,N+1):
    list1.append(i)
print(list1)

people_list = list(range(1, N + 1))
out = 0

for i in range(N - 1):
    print('Текущий круг людей', people_list)
    start_count = out % len(people_list)
    out = (start_count + K - 1) % len(people_list)
    print('Начало счёта с номера', people_list[start_count])
    print('Выбывает человек под номером', people_list[out])
    people_list.remove(people_list[out])

print('Остался человек под номером', people_list)