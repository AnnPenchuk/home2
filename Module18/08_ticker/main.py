str1=input('Первая строка: ')
str2=input('Вторая строка: ')
count=0
str=''
for i in range(len(str2)):
    str=str2[-1:]+str2[:-1]
    print(str)
    if str==str1:
        print('Первая строка получается из второй со сдвигом ',i+1)
        break
    else:
        count+=1
    str2 = str
    str = ''
if count==len(str2):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
