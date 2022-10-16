IP=input('Введите IP: ')
str=IP.split('.')
print(str)
def is_good_len(str):
    if len(str)!= 4:
        print('aдрес - это четыре числа, разделённые точками')
    return len(str)

def is_int(str):
    count= 0
    for i in str:
        if not i.isdigit():
               print(i, ' это не целое число.')
               count += 1
    return count

def is_range(str):
    count1=0
    for i in str:
        if  int(i)<0:
                print(i,'должно быть больше 0')
                count1 += 1
        if int(i) > 255:
            print(i, 'должно быть меньше 255')
            count1 += 1
    return count1

if is_good_len(str)== 4 and is_int(str)==0 and is_range(str)==0:
    print('IP-адрес корректен.')