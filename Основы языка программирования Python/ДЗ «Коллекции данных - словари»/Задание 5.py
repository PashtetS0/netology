s = ['2018-01-01', 'yandex', 'cpc', 100]

*_, d = s
for i in range(len(s)-1, 0, -1):
    d = {s[i-1]: d}
print(d)
print('==============')
d = s[-1]
[d := {s[i-1]: d} for i in range(len(s)-1, 0, -1)]
print(d)
print('==============')
d = s[-1]
[d := {i: d} for i in s[-2::-1]]
print(d)
