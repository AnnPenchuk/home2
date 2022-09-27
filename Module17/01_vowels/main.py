
alphabet='аеёиоуэюя'
text=input('Введите текст:')

new = [i for i in text if i in alphabet]

print(new)
print('длина списка',len(new))
