#! C:\python27
from collections import Counter

cnt = Counter ();

for line in open('words.txt', 'r'):
 for word in line.split ():
     cnt [word] += 1

print (cnt)
