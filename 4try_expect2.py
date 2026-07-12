x = 0
rawstr = input('enter a number:')
try:
    ival = int(rawstr)
except:
    x = -1
if x == 0:
    print('Nice work')
else:
    print('Not a number')
#注：原程序是在except中使用ival = -1，if中使用ival > 0，这会导致在line2输入负数时显示Not a number