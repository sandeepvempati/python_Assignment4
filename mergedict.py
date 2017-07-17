dict1 = {'a':1,'b':2,'c':3,'d':4}
dict2 = {'e':5,'f':6,'g':7,'h':8}

for i in dict2:
    if i not in dict1:
        d = {i:dict2[i]}
        dict1.update(d)

print dict1


# dict1.update(dict2)
# print dict1

# print dict(dict1,**dict2)

print dict(dict1.items()|dict2.items())
