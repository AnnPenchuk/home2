numbers=(1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
n = int(input('введите элемент '))

def slicer(numbers,n):
    if n not in numbers:
        return ()
    if numbers.count(n) == 1:
        return numbers[numbers.index(n):]
    return numbers[numbers.index(n):numbers.index(n, numbers.index(n) + 1) + 1]

print(slicer(numbers,n))

