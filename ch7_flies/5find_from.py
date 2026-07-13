fname = open('ch7_flies\mbox.txt')
for line in fname:
    if line.startswith('From:'):
        line = line.rstrip()#每一行本身就有/n，rstrip()去掉每一行末尾的换行符，print()会自动在每一行末尾加上换行符，所以不需要再加/n
        print(line)