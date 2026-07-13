name = input('enter a file:')
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] =counts.get(word,0) + 1
Big_count = None
Big_word = None
for word,count in counts.items():
    if Big_count is None or count > Big_count:
        Big_count = count
        Big_word = word
print(Big_word,Big_count)