n = int(input("введите n "))
print(n)

i = 1
print(i)

sum = 0
print(sum)

while i <= n:

    sum = sum + i**3
    print(sum, i, n)
    i = i + 1


else:
    print("end")