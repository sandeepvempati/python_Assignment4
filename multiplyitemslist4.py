li = []
for i in range(int(raw_input("Enter the length of list"))):
    li.append(int(raw_input()))

# li = map(int,raw_input("enter the values in the list").split())
x=1
for i in li:
    x *= i
print x