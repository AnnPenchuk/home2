

alphabet='абвгдеёжзийклмнопрстуфчцчшщъыьэюя'
message=input('Введите сообщение:')
shift=int(input('Введите сдвиг:'))
#list1=[(alphabet[(alphabet.index(i)+shift)%len(alphabet)] if i!=' ' else ' ') for i in message]
list1=[(alphabet[(alphabet.index(i)+shift)%len(alphabet)] if i in alphabet else i) for i in message]
new=''
for x in list1:
    new+=x
print(new)
