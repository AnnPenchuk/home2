'''''
string=input('Введите строку: ')
char_dict={}
for i in string:
    char_dict[i]=char_dict.get(i,0)+1
count=0
for value in char_dict.values():
    if value % 2!=0:
         count+=1

if count<=1:
    print('Можно сделать палиндромом.')
else:
    print('Нельзя сделать палиндромом.')


'''


def check_number(number):
    return count_number_len(number) > 4

def count_number_len(x):
    count = 0
    while x:
        count += 1
        x //= 10

x = 1234
if check_number(x):
    print("1")
else:
    print("2")