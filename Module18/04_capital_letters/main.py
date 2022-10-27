string=input('Введите строку: ')
word_list=string.lower().split()
word_list2=[]
print(word_list)
for i in word_list:
    i=i[0].upper()+i[1:]
    word_list2.append(i)
print(' '.join(word_list2))