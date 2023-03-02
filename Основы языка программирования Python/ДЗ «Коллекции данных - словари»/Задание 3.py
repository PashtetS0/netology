queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

all_requests = len(queries)
d = {}
[d.setdefault(len(elem.split()), []).append(elem) for elem in queries]
for key, value in sorted(d.items()):
    print(f'Из количества слов в запросе равным {key} состоит {len(value) / all_requests * 100:.3f}% запросов')