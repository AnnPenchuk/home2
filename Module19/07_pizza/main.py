N=int(input('Введите количество заказов: '))
value_inf={}

for i in range(1,N+1):
    value = input('{} заказ: '.format(i)).lower().split()
    #print(value)
    pizza=value[1]
    count=int(value[2])
    if value[0] in value_inf:
        if value[1]==value_inf[value[0]]:
           value_inf[value[0]][pizza] += count
        else:
            value_inf[value[0]][pizza] = count
    else:
             value_inf[value[0]] = {pizza: count}


    for value[0], order in sorted(value_inf.items()):
        print(f'{value[0]}:')
        for pizza,count in sorted(order.items()):
            print('\t', pizza, count)



