
import os

fpath = os.path.join("e:","text1.txt")
print(fpath)
try:
    f = open(fpath, "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("No such file or directory")


