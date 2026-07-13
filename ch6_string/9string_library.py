#str.capitalize() method returns a copy of the string with its first character capitalized (only first character) and the rest lowercased.
print('after using capitalize() method, hello bob becomes: ', 'hello bob'.capitalize())
print('after using capitalize() method, abc becomes: ', 'abc'.capitalize())
print('after using capitalize() method, ABC becomes: ', 'ABC'.capitalize())
#find() method returns the lowest index of the substring if it is found in given string. If it is not found, it returns -1.
fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find ('z')
print(aa)
#find() returns index of the first character
#upper() and lower() methods return a copy of the string in which all case-based characters have been uppercased or lowercased and return it to us.
greet = 'Hello Bob'
nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www)
#replace() method returns a copy of the string in which all occurrences of a substring are replaced with another substring.
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o', 'x')
print(nstr)
#lstrip() method returns a copy of the string in which all leading whitespaces are removed.
greet = '   Hello Bob   '
print(greet)
print(greet.lstrip())
#rstrip() method returns a copy of the string in which all trailing whitespaces are removed.
print(greet.rstrip())
#strip() method returns a copy of the string in which all leading and trailing whitespaces are removed.
print(greet.strip())
print(greet)  #to show that the original string is not changed, we print it again.