guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

count=len(guests)
print('сейчас на вечеринке, ',count, 'человек:', guests)
action = input('Гость пришёл или ушёл? ')
while action!='пора спать':
            if action=='пришел':
                name=input('имя гостя')
                сount = len(guests)
                if count<6:
                     print('привет, ',name)
                     guests.append(name)
                else:
                     print('прости, ', name, ', но мест нет.')
            elif action=='ушел':
                 name = input('имя гостя')
                 print('пока, ',name)
                 guests.remove(name)
            count = len(guests)
            print('сейчас на вечеринке, ', count, 'человек:', guests)
            action = input('Гость пришёл или ушёл? ')
print('Вечеринка закончилась, все легли спать.')