contact = dict()
while True:
    print('1. Добавить контакт.')
    print('2. Найти человека ')
    n=int(input('введите номер действия: '))
    if n==1:
        fi=input('Введите имя и фамилию нового контакта (через пробел):').split()
        print(fi)
        f=(fi[0],fi[1])
        contact[f]=input('Введите номер телефона: ')
        print('Текущий словарь контактов:', contact)
    if n == 2:
        fam = input('введите фамилию ')
        for i_person in contact:
            if fam in i_person:
                print(i_person, contact[i_person])

#работвет