a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
print('первый закинули в основной',a)
count5=a.count(5)
#print(count5)

while count5>0:
      a.remove(5)
      count5-=1
print('получили',a)

a.extend(c)
print('второй закинули в основной',a)
count3=a.count(3)
#print(count3)
while count3>0:
      a.remove(3)
      count3-=1
print('получили',a)



