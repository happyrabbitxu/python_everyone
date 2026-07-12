astr = 'HELLO'
try:
    istr = int(astr)
except:
    istr = -1
print('first', istr)
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('second', istr)
#try_except:如果try中的代码（块）出现错误（回溯），程序会执行except中的代码，except有点像else