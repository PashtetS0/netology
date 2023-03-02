geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

# s = []
# for i in geo_logs:
#     for value in i.values():
#         if 'Россия' in value:
#             s.append(i)
# print(s)

# for id, i in enumerate(geo_logs, start=0):
#     for value in i.values():
#         if 'Россия' not in value:
#             geo_logs[id] = 'tmp'
# while 'tmp' in geo_logs:
#     geo_logs.remove('tmp')
# print(geo_logs)

print([i for i in geo_logs if 'Россия' in list(*i.values())])