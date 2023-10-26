import os

fpath = os.path.join("e:", "text.txt")
f = open(fpath, "r")
fpath1 = os.path.join("e:", "text1.txt")
f1 = open(fpath1, "w")
f1.write(f.read())
f.close()
f1.close()