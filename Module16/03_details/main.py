shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]



detail=input('введите название детали ')

sum=0
price=0
count=0
for i in shop:
      if i[0]==detail:
          count+=1
          price+=i[1]
print('количество',count)
print('общая стоимость',price)
