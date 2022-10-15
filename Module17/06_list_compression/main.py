
N=int(input('количество чисел в списке'))
list1=[int(input('')) for x in range(N)]

print('Список до сжатия:',list1)
list2=[]
for i in list1:
    if i!=0:
       list2.append(i)
print('Список после сжатия:',list2)
