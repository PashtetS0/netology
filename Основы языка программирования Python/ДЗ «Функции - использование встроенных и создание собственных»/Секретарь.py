from pprint import pprint

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def name_by_number(people):  # команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
    # return str(*[i['name'] for i in documents if i['number'] == people])
    # return ''.join([i['name'] for i in documents if i['number'] == people])
    name = [i['name'] for i in documents if i['number'] == people]
    # return str(*name) if name else f'По введенному номеру документа "{people}" ничего не найдено.'
    return f'\nПо покументу "{people}" данные на имя - "{"".join(name)}"' if name \
        else f'\nПо введенному номеру документа "{people}" ничего не найдено.'
# print(name_by_number(input('Введите номер документа - ')))

def shelf_number(shelf):  # команда, которая спросит номер документа и выведет номер полки, на которой он находится;
                          # Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
    sh = [k for k, v in directories.items() if shelf in v]
    return f'\nДокумент "{shelf}" находится на полке - "{"".join(sh)}"' if sh \
         else f'\nПо введенному номеру документа "{shelf}" ничего не найдено.'
# print(shelf_number(input('Введите номер документа - ')))

def list_of_all_documents():  # команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    # [[a, b, c for a, b, c in i.values()] for i in documents]
    # ls = [[*i.values()] for i in documents]
    # ls = [i.values() for i in documents]
    # print(*ls)
    return [[*i.values()] for i in documents]  # "выведет список всех документов в формате passport "2207 876234" "Василий Гупкин""

    # for i in documents:
        # print(*list(i.values()))
        # return list(i.values())
        # for a, b, c in list(i.values()):
        #     print(a, b, c)
# print(*list_of_all_documents(), sep='\n')

def new_document(*args):  # команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
                          # имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию,
                          # когда пользователь будет пытаться добавить документ на несуществующую полку.
    n_type, n_number, n_name, shelf = args
    if 1 <= int(shelf) <= maxi_shelf:
        documents.append({"type": n_type, "number": n_number, "name": n_name})
        directories.setdefault(shelf, []).append(n_number)
        return f'\nДанные {n_type, n_number, n_name} внесены в новый каталог на полку "{shelf}".'
    else:
        return f'\nВы ввели несуществующую полку "{shelf}" полок всего "{maxi_shelf}".'
# maxi_shelf = len(directories)
# print('Последовательно введите запрашиваемые данные:')
# print(f'тип документа, номер документа, имя владельца и номер полки (числом) 1 - {maxi_shelf}\n')
# print(new_document(*[input('Ввод - ') for _ in range(4)]))

def delete_document(delete):  # команда, которая спросит номер документа и удалит полностью документ из каталога и его номер из перечня полок.
                              # Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
    k = ''.join([k for k, v in directories.items() if delete in v])
    if k:
        directories.setdefault(k, []).remove(delete)
        del documents[int(*[i for i in range(len(documents)) if delete in documents[i]['number'] == delete])]
        return f'\nДанные по введенному номеру документа "{delete}" удалены.'
    else:
        return f'\nПо введенному номеру документа "{delete}" данных не найдено.'
# print(delete_document(input('Введите номер документа для удаления - ')))

def move_document(*args):  # команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
                           # Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ
                           # или переместить документ на несуществующую полку;
    number, shelf = args
    current = ''.join([k for k, v in directories.items() if number in v])
    if current and 1 <= int(shelf) <= maxi_shelf and current != shelf:
        ind = directories.setdefault(current, []).index(number)
        directories.setdefault(shelf, []).append(directories[current].pop(ind))
        return f'\nДокумент "{number}" успешно перемещен на полку "{shelf}".'
    else:
        # print(f'\nТекущая полка с документом {current}') if current else None
        return f'\nПроверьте введенные данные - документ "{number}", полка "{shelf}"\n\
либо документ не существует, либо такой полки нет "1 - {maxi_shelf}"\n\
либо номер полки для премещения совпадает с текущей.'
# maxi_shelf = len(directories)
# print('Последовательно введите запрашиваемые данные:')
# print(f'номер документа и номер полки (числом) 1 - {maxi_shelf}\n\
# на которую нужно преместить документ.\n')
# print(move_document(*[input('Ввод - ') for _ in range(2)]))

def add_shelf(add_shelf):  # команда, которая спросит номер новой полки и добавит ее в перечень.
                           # Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.
    if 1 <= int(add_shelf) <= maxi_shelf or int(add_shelf) <= 0:
        return f'\nВы ввели неверный номер полки - "{add_shelf}".'
    else:
        directories.setdefault(add_shelf, [])
        return f'\nПолка "{add_shelf}" успешно добавлена и доступна для использования.'

# maxi_shelf = len(directories)
# print(f'Существующие на данный момент полки "1 - {maxi_shelf}"')
# print(add_shelf(input(f'Введите номер новой полки (> {maxi_shelf}) для добавления - ')))
print('=====================================')
print(documents)
pprint(directories)
