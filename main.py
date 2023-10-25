
# word = "summer"
# try:
#     print(word[3])
#     print(word[6])
# except IndexError:
#     print("incorrect index")
#
# a = input()
try:
    a = float(input("Input number 1: "))
    b = float(input("Input number 2: "))
except ValueError:
    print("incorrect value")

