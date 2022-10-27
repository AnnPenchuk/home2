N=int(input('сколько стран? '))
data_set = {}
for i in range(N):
    value = input('{} страна: '.format(i + 1)).split()
    for x in value[1:]:
        data_set[x] = value[0]

for i in range(3):
    city = input('\n{} город: '.format(i + 1))
    country = data_set.get(city)
    if country:
        print(f'Город {city} расположен в стране {country}.')
    else:
        print(f'По городу {city} данных нет.')



