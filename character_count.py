from collections import Counter

with open('CombinedPasswords.txt') as f:

    c = Counter()
    for x in f:
        c += Counter(x.strip())
print c
