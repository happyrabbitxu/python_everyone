counts = {'a':1,'b':2,'c':3}
while True:
    name = input('enter a,b,or c to check its value,tpye done to exit\n')
    if name == 'done':quit()
    x = counts.get(name,0)#若不存在这个key则为0
    print(x)
#if name in counts:
#    x = counts[name]
#else:
#    x = 0
#这段代码与x = counts.get(name,0)等价