import os

fpath = os.path.join("e:", "text.txt")
f = open(fpath, "w")
mystr = str(input("input your string:"))
f.write(mystr)
f.close()
