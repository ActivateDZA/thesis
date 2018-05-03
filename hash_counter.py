#! C:\python27
from collections import Counter
import csv

cnt = Counter ();
write_file = "output.csv"

with open(write_file,"w") as output:
    for line in open('E:\\Pentesting\\NTDS hashes\\combined_lm_ntlm.txt', 'r'):
        for word in line.split ():
            cnt [word] += 1
    for k,v in cnt.most_common():
        output.write( "{}, {}\n".format(k,v) )
