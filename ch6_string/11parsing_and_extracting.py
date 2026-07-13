data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpots = data.find('@')                                          #We want to find the host,which is after '@' and before the next space. So we find the index of '@'  
print(atpots) 
sppots = data.find(' ', atpots)                                  #then find the index of the next space after @.
print(sppots)
host = data[atpots+1:sppots]
print(host)
#we can give the find() method two arguments-what to find and where to start looking. The second argument is a index
#because [] means[),so just before the space-the host 