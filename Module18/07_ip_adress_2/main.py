IP=input('Введите IP: ')
str=IP.split('.')
count=0

if len(str) < 4:
    print('aдрес - это четыре числа, разделённые точками')
    count+=1

else:
    for i in str:

       if i.isdigit():


           if int(i)<0:
                print(i,'меньше 0')
                count += 1
                break
           elif int(i)>255:
                print(i, 'больше 255')
                count += 1
                break


       else:
            print(i, ' это не целое число.')
            count+=1
if count<1:
    print('IP-адрес корректен.')