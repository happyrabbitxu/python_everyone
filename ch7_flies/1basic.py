#open() is just a handle to a file on disk. It is not the file itself. You can read or write to the file by calling methods on the handle. The file handle is also called a stream.
#open() takes two arguments: the first is the name of the file, 
# and the second is a string that specifies whether you want to read or write the file. The string 'r' indicates that we want to read the file, 
# and 'w' indicates that we want to write the file. If you omit the second argument, it will assume that you want to read the file.

import os
print(os.getcwd())
fhandle = open('\mbox-short.txt') 
print(fhandle) 
#use \n to a new line
#在交互模式中若 x = 'aaa\nbbb'则输入x会返回aaa\nbbb，而print(x)会返回aaa
#bbb。因为print()会把\n解释为换行符，而在交互模式下，\n只是一个普通的字符。
