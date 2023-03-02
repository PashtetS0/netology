boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', '']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) == len(girls):
    girls.sort()  # Почему если сортировку через метод .sort() вставить в zip() дает ошибку? А функция sorted() не дает?
    print('Идеальные пары:')
    for i, j in zip(sorted(boys), girls):
        print(f'{i} и {j}')
else:
    print('Kто-то может остаться без пары!')