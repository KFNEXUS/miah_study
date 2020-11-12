def find(str, ch):
    index = 0
    while index < len(str):
        print(str[index], index, ch)
        if str[index] == ch:
            return index
        index = index + 1

    return -1

c = find('hgfhdg', 'f')
print(c)
