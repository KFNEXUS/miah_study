def sum(n):
    if n == 1:
        return 1
    else:
        return (n ** 3) + sum(n - 1)


print(sum(4))