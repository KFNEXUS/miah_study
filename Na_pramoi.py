import math
print(abs(-100))
##нахождение расстояния между точками на прямой
print('Пожалуйста под x1 напишите большее число')
print('модуль x1-x2')
x1 = int(input("введите x1 "))
x2 = int(input("введите x2 "))
x = math.sqrt((x1-x2)**2)
print('x = ' + str(x))