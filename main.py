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
fpath1 = os.path.join("e:", "text1.txt")
f1 = open(fpath1, "w")
f1.write(f.read())
f.close()
f1.close()
