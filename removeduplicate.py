li = map(int,raw_input("Enter the values in the lsit").split())
li2 = []

for i in li:
    if i not in li2:
        li2.append(i)

print li2
