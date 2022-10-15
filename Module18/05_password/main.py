
digits=0
count=0
while True:
    password=input('Придумайте пароль: ')
    for i in password:
        if i.isnumeric():
            digits+=1
        if i.isupper():
            count+=1

    if len(password)<8:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    elif digits<3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    elif count<1:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break






