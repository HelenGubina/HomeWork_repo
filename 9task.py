import os

fpath = os.path.join("e:", "text.txt")
f = open(fpath, "r")
linenumber = int(input("input number of line for deletion:"))
list1 = f.readlines()
list1.remove(list1[linenumber])
f.close()
f = open(fpath, "w")
strnew = ""
for line in list1:
    strnew += line

f.write(strnew)
f.close()
