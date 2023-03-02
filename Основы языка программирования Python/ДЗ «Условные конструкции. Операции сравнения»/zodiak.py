print('Западная астрология (вариант II):\n')

month = input('Введите название месяца по-русски в именительном падеже - ').lower()
date = int(input('Введите день месяца (числом от 1 до 31) - '))
if month == 'февраль' and date == 29:
  print('\nЗнак зодиака \u2653 - Рыбы')
elif ((21 <= date <= 31 and month == 'март')
      or (1 <= date <= 20 and month == 'апрель')):
  print('\nЗнак зодиака \u2648 - Овен')
elif ((21 <= date <= 30 and month == 'апрель')
      or (1 <= date <= 21 and month == 'май')):
  print('\nЗнак зодиака \u2649 - Телец')
elif ((22 <= date <= 31 and month == 'май')
      or (1 <= date <= 21 and month == 'июнь')):
  print('\nЗнак зодиака \u264A - Близнецы')
elif ((22 <= date <= 30 and month == 'июнь')
      or (1 <= date <= 22 and month == 'июль')):
  print('\nЗнак зодиака \u264B - Рак')
elif ((23 <= date <= 31 and month == 'июль')
      or (1 <= date <= 21 and month == 'август')):
  print('\nЗнак зодиака \u264C - Лев')
elif ((22 <= date <= 31 and month == 'август')
      or (1 <= date <= 23 and month == 'сентябрь')):
  print('\nЗнак зодиака \u264D - Дева')
elif ((24 <= date <= 30 and month == 'сентябрь')
      or (1 <= date <= 23 and month == 'октябрь')):
  print('\nЗнак зодиака \u264E - Весы')
elif ((24 <= date <= 31 and month == 'октябрь')
      or (1 <= date <= 22 and month == 'ноябрь')):
  print('\nЗнак зодиака \u264F - Скорпион')
elif ((23 <= date <= 30 and month == 'ноябрь')
      or (1 <= date <= 22 and month == 'декабрь')):
  print('\nЗнак зодиака \u2650 - Стрелец')
elif ((23 <= date <= 31 and month == 'декабрь')
      or (1 <= date <= 20 and month == 'январь')):
  print('\nЗнак зодиака \u2651 - Козерог')
elif ((21 <= date <= 31 and month == 'январь')
      or (1 <= date <= 19 and month == 'февраль')):
  print('\nЗнак зодиака \u2652 - Водолей')
elif ((20 <= date <= 28 and month == 'февраль')
      or (1 <= date <= 20 and month == 'март')):
  print('\nЗнак зодиака \u2653 - Рыбы')
else:
  print('\nНеверный ввод')
