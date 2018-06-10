#! C:\python27
from collections import Counter
import csv

cnt = Counter (); #counter
write_file = "output.csv" # file name for output

with open(write_file,"w") as output: # reading file that contains the hashes
    for line in open('combined_lm_ntlm.txt', 'r'): #file location that contains the hashes
        for word in line.split (): #read the open file
            cnt [word] += 1 # counter for hashes
    for k,v in cnt.most_common():
        output.write( "{}, {}\n".format(k,v) ) #output format that will be written to write_file
