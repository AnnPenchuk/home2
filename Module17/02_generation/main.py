N=int(input('введите длину списка '))

nums=[(1 if x %2==0 else x%5)for x in range(N)]

print(nums)
