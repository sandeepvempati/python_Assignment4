d={'a':1,'b':2,'c':3,'d':4}

def dict_has_key(x):
    if x in d.keys():
        print " Given Key '%s' in dictionary" %x
    else:
        print "Given Key '%s' is not present in dictionary" %x

dict_has_key(raw_input())
