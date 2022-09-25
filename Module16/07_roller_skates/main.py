N=int(input('количество коньков:'))
skates=[]
for i in range(N):
    a=int(input('введите размер пары'))
    skates.append(a)
print('1',skates)


K=int(input('введите КОЛИЧЕСТВО ЛЮДЕЙ:'))
people=[]
for i in range(K):
    b=int(input('введите размер ноги'))
    people.append(b)
print('2',people)


count=0
for foot in people:
    if foot in skates:
        skates.remove(foot)
        count += 1
print('Наибольшее кол-во людей, которые могут взять ролики:', count)
