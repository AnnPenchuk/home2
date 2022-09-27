N=int(input('введите длину '))
str=[(input('')) for x in range(N)]
print(str)
h1=str.index('h')
h2=str[h1+1:N].index('h')
print('Развёрнутая последовательность между первым и последним h:',str[h2:h1:-1])

