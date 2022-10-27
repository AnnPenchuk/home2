N=int(input('количество пар слов: '))
data = {}
for i in range(N):
    value = input('{} пара: '.format(i + 1)).lower().split()
    for x in value[1:]:
        if x=='—':
            continue
        else:
          data[x] = value[0]

print(data)

for i in range(2):
    word = input(' Введите слово ')
    cin= data.get(word)
    if cin:
        print(f'синоним {cin} .')
    else:
        print('Такого слова в словаре нет.')
