smallest = None   #flag variable to indicate that we have not found any value yet
print('before', smallest)
for value in [9,41,12,3,74,15]:
    if smallest is None or value < smallest:         #or use if smallest is None:        for prime(初始化)
        smallest = value                             #           smallest = value    
                                                     #       elif value < smallest:
                                                     #           smallest = value
    print('after', smallest)                         
print('after', smallest)                             
#The difference between is and == is that is checks for identity, while == checks for equality. In this case, we want to check if smallest is None, which means that we have not found any value yet. If we used == instead of is, it would check if smallest is equal to None, which would not be the same thing.
#"Is" is more strick than "==", for example,1 == 1.0 is true, but 1 is 1.0 is false. 