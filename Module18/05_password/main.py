

def is_good_len(password):
    return len(password)


def is_isnumeric(password):
    digits = 0
    for i in password:
        if i.isnumeric():
            digits += 1
    return digits


def is_isupper(password):
    count = 0
    for i in password:
        if i.isupper():
            count += 1
    return count



while True:
    password=input('Придумайте пароль: ')


    if is_good_len(password)>8 and is_isnumeric(password)>=3 and is_isupper(password)>=1:
         print('Это надёжный пароль!')
         break

    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')

