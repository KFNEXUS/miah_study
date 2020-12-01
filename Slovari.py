eng2sp = {}
eng2sp2 = {'one': 'uno', 'two': 'dos', 'abs': 'las'}

for (k,v) in eng2sp2.items():
    print("Got",k,"that maps to",v)

eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
del eng2sp['two']
print(eng2sp)

matrix = {(1, 1): 1, (10, 10): 5}
print(matrix.keys())
print(matrix.values())
print(matrix.get((1, 10), 0))
copy = matrix.copy()
print(copy)
temp = list(eng2sp2.items())
print(temp.sort())
print(temp)