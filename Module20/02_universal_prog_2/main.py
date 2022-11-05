text=input('Введите текст:')


def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return 0
    return 1



new_text=[]
for i in range(len(text)):
    if is_prime(i)==1:
        new_text.append(text[i])
print(new_text)


