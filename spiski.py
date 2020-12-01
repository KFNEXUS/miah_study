import string

spisok = [10, ]
print(len(spisok))
spisok_4isla = [10, 20, 30, 40]

print(spisok_4isla)
spisok_4isla[1:1] = [1,2,3]
print(spisok_4isla)
spisok_4isla.append(1000)

print(1000 in spisok_4isla)
print(spisok_4isla)
del spisok_4isla[-1]
print(spisok_4isla)
#Копирование списка
b = spisok_4isla[:]


print(b)

print(spisok_4isla[-1])
sp_r = range(9)
print(sp_r)

spisok_slov = ['raz', 'dva', 'tri']
print(spisok_slov)

spisok_vlojenii = [10, 20, 30,[10, 20, 30, 40]]

print(spisok_vlojenii[3][1])
print(list("Crunchy Frog"))
print("----".join(spisok_slov))
