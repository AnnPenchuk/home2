N=int(input(' количество друзей:'))
K=int(input('количество долговых расписок:'))

friends_list = []

for i in range(N):
    friends_list.append(0)

for number in range(K):
        print(number + 1,'расписка')
        to_who = int(input('Кому: '))
        from_who = int(input('От кого: '))
        how_much = int(input('Сколько: '))
        friends_list[from_who - 1] += how_much
        friends_list[to_who - 1] -= how_much

print('Баланс друзей:')
for j in range(len(friends_list)):
    print('друг',j + 1,'его баланс',friends_list[j])

