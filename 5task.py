import os

fpath = os.path.join("e:", "text.txt")
f = open(fpath, "r")
mystr = f.read()
mylist = mystr.split()
print(len(mylist))