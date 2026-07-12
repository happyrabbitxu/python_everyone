while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done': 
        break
    print(line)
print('Done')
#continue出现，运行到它后循环直接跳过本次循环，继续下一次循环，即返回到循环开始判断的位置，从头开始循环
#下列为运行结果
'''
>aaa
aaa
>bbb
bbb
>#不要输出这个
>done
Done'''