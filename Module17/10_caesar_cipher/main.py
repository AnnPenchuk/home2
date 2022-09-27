
alphabet='абвгдеёжзийклмнопрстуфчцчшщъыьэюя'
message=input('Введите сообщение:')
shift=int(input('Введите сдвиг:'))
list1=[(alphabet[(alphabet.index(i)+shift)%33] if i!=' ' else ' ') for i in message]
new=''
for x in list1:
    new+=x
print(new)