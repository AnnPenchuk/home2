family = {
    ('сидоров', 'никита'): 13,
    ('сидорова', 'алина'): 14,
    ('сидоров', 'павел'): 38,
    ('иванов', 'слава'): 45,
    ('иванова', 'маша'): 37,
    ('петров', 'иван'): 89,
    ('петрова', 'катя'): 23,
}


fam=input('введите фамилию ').lower()
for i_person in family:
    if i_person[0].startswith(fam):
        print(i_person[0], i_person[1], family[i_person])

##работает