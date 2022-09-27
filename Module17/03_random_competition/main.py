import random

list1=[round(random.uniform(1, 10), 2) for i in range(5)]
print(list1)
list2=[round(random.uniform(1, 10), 2) for j in range(5)]
print(list2)
list3=[]
for x in range(5):
        if list1[x]>list2[x]:
            list3.append(list1[x])
        else:
            list3.append(list2[x])

print('Победители тура',list3)
