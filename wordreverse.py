n=raw_input()
txt=""
for i in range(len(n)-1,-1,-1):
    txt += n[i]
print txt


# n = raw_input()
# print "".join((str(n[i]) for i in range(len(n)-1,-1,-1)))


# print "".join((str(i) for i in range(5)))