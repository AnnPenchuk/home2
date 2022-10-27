string=input('Введите строку: ')
str=string.split()
m=max(str, key = len)
print('Самое длинное слово:  ',m,'Длина этого слова: ',len(m))