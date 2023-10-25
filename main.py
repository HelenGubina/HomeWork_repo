#
# a = float(input("input number 1:"))
# b = float(input("input number 2:"))
# try:
#     c = a / b
#     print(c)
# except ZeroDivisionError:
#     print("You can divide by zero")

import os

fpath = os.path.join("e:", "text.txt")
f = open(fpath, "r")
mystr = f.read()
mylist = mystr.split()
print(len(mylist))
