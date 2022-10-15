
s=input('Введите строку: ')
j=s[0]
count=0
res=''
for i in s:
    print(i)
    #print
    #count += 1
    if i==j:
        #print(count)
        count+=1
        #res+=str(count)
    else:
        res+=j
        j = i
        res += str(count)
        count=1
res+=j
res += str(count)
print(i)
print(count)
print('Закодированная строка: ', res)

