import os

fpath = os.path.join("e:", "text.txt")
f = open(fpath, "r")
fpath1 = os.path.join("e:", "text1.txt")
f1 = open(fpath1, "r")
list1 = f.readlines()
list2 = f1.readlines()
for line in list1:
    try:
        if line != list2[list1.index(line)]:
            print(line)
    except IndexError:
        print(line)
f.close()
f1.close()
