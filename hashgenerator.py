#! C:\python27
import string, random,hashlib,binascii
special = ["-","_","!","@","*","$",".","?"]
with open('words.txt') as words:
 for line in words:
     if len(line)>=8:
         special= random.choice(special)
         capitalized_string = line.capitalize()
         full = capitalized_string+special
         #print full
         hash = hashlib.new('md4', full.encode('utf-16le')).digest()
         print binascii.hexlify(hash)
