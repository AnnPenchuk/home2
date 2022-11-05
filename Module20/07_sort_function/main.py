tup1=[-3, -5, 7.6, 10, 9, -5.3, 3.4, -6, 5, 1]
tup2=[-3, -5, 7, 10, 9, -5, 3, -6, 5, 1]

def tpl_sort(tup):
    list=[]
    for i in tup:
        if i-int(i)==0:
            list.append(i)
        else:
            list=tup
            break
        list=sorted(list)
    return list

print(tpl_sort(tup1))
print(tpl_sort(tup2))

#работает