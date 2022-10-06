
vowels='аеёиоуэюя'
text=input('Введите текст:')

new = [i for i in text if i in vowels]

print(new)
print('длина списка',len(new))
 