import math

def D(a,b,c):
    sum = (b**b)-(4*a*c)

    return sum

def x1(a,b,func):
    sum = (-b + math.sqrt(func)) / (2 * a)

    return sum

def x2(a,b,func):
    sum = (-b - math.sqrt(func)) / (2 * a)

    return sum

    print(x1(1,2,D(1,2,3))))