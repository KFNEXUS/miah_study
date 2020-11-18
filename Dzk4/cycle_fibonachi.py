n = int(input('n = '))
i = 0
while i <= n:
    print(i, n, n - 1, n - 2)
    i = i + 1
    n = (n - 1) + (n - 2)
print(n)
