count = 0
sum = 0
print('before', count, sum)
for value in [9,41,12,3,74,15]:
    count = 1 + count
    sum = sum + value
    print(count, sum, value)
print('平均值使用int取整,直接抹掉小数')
print('after',count,sum,int(sum/count))#没有int会显示25.6666666
print('平均值不使用int取整,保留小数')
print('after',count,sum,sum/count)