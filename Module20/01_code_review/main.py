

def foo(d: dict) -> tuple:
    return [d[i]['age'] for i in d], set(sum([d[i]['interests'] for i in d], [])), sum(map(len, [d[i]['surname'] for i in d]))


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food', 'running']
    }
}

age, interests, total_len = foo(students)
print('ID студента — возраст',list(zip(students.keys(),age)))
print('Полный список интересов всех студентов:',', '.join(interests))
print('Общая длина всех фамилий студентов: ',total_len)

#работает