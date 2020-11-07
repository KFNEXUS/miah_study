import math

print('ax^2+bx+c')
a = int(input("введите a "))
b = int(input("введите b "))
c = int(input("введите c "))

def cvadrat(a, b, c):
    D = (b ** 2) - (4 * a * c)
    if D < 0:
        print('Уравнение не имеет корней')
        return None, None
    elif D == 0:
        x = -b / (2 * a)
        print('x = ' + str(x))
        return x, None
    else:
        kD = math.sqrt(D)
        x1 = (-b + kD) / (2 * a)
        x2 = (-b - kD) / (2 * a)
        print('x1 = ' + str(x1) + ' x2 = ' + str(x2))
        return x1, x2

x1, x2 = cvadrat(a, b, c);