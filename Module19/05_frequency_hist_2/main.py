text=input('Введите текст:')
char_dict={ }
dict=[]
for i in text:
    char_dict[i]=char_dict.get(i,0)+1

for i in range(1,max(char_dict.values())+1):
    for value,key in char_dict.items():
           if key==i:
               dict.append(value)
    print(i,':',dict)
    dict=[]
