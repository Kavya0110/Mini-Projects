l1 = [9, 8, 7, 6, 5, 4]
x= 5
def search():
    for i in range(len(l1)):
        if l1[i] == x:
            return i


print(search())


