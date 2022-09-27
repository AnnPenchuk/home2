list1=[]
for i in range(3):
    a=int(input('введите числа'))
    list1.append(a)
print('1',list1)

list2=[]
for i in range(7):
    b=int(input('введите числа'))
    list2.append(b)
print('2',list2)

list1.extend(list2)
print(list1)

new=[]
for number in list1:
    if number in new:
        continue
    else:
        new.append(number)
print(new)
