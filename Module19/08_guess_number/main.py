
N=int(input('Введите максимальное число: '))
data = set()
v = input('Нужное число есть среди вот этих чисел:  ')
value=v.split()
print(value)
while v!='Помогите!':
        answer= input('Ответ Артёма: ')
        if answer=='да':
            data.update(value)

        if answer=='нет':
            data=data.difference(value)

        v = input('Нужное число есть среди вот этих чисел:  ')
        value = v.split()
print('Артём мог загадать следующие числа: ',data)

