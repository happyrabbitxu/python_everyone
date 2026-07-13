s = 'Monty Python'
print(s[0:4])   #index 0 is included, index 4 is not included
print(s[6:7])   #index 6 is included, index 7 is not included
print(s[6:20])  #index 6 is included, index 20 is not included
#'[]'includes the first index and excludes the last index. If the last index is greater than the length of the string, it will just go to the end of the string.
#The thing changes when there are no numbers in the brackets. If there is no first number, it will start from the beginning of the string. If there is no second number,
#  it will go to the end of the string.
print('The next three codes')
print(s[ :2])
print(s[8: ])
print(s[ : ])