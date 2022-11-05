
list=[3, 5, 7, 10, 9, 5, 3, 6, 5, 1]
print(list)
list1=[]
list2=[]

s=0
j=list[0]
for i in list[1:]:
    s=(j,i)
    if i!=j:
      list1.append(s)
      j=i
list2=list1[::2]
print(list2)

#аботает