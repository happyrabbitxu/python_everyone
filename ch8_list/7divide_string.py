abc = "with three words"
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)
    #in split()more space epual to one space"       with   more      space"
abc = "       with   more      space"
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)
#split() allows an argument to tell itself which  is the symbol of split(分割)
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(';')
print(thing)
print(len(thing))