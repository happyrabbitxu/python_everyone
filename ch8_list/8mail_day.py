fhand =open('ch7_flies/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):continue
    words = line.split()
    if words[2] != 'this':
        print(words[2])