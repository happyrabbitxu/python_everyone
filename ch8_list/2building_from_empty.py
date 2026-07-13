stuff = list() #create an empty list the same as stuff = []
stuff.append('book') #add an item to the end of the list
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)
#do not use stuff = stuff.append('cookie') because append() does not return a value, it modifies the list in place and returns None.