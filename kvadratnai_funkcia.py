print('Пограмма для нахождения значений графика квадратичной функции')

print('f(y)=ax^2+bx+c')

a = int(input('введите a '))
b = int(input('введите b '))
c = int(input('введите c '))
minx = int(input('введите минимальное значение x '))
maxx = int(input('введите максимальное значение x '))

while minx <= maxx:
    y = (a * (minx ** 2)) + (b * minx) + c
    print('x = ' + str(minx), 'y = ' + str(y))
    minx = minx + 1

else:
    print('end')
