xfile=open('ch7_flies/mbox.txt')
for cheese in xfile:
 #   print(cheese)
fhand=open('ch7_flies/mbox-short.txt')
inp=fhand.read()
print(len(inp))
print(inp[:20])
