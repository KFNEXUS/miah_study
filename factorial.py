def fact(n):
    print(n, (n-1)*n, (n-1))
    if n == 0:
        return 1
    else:
        return fact(n-1)*n

print(fact(7))