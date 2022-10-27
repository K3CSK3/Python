from os import system
number :int = None

print("Adjon meg egy számot: ",end='')
number = int(input())

system('cls')

if ((number % 2) == 0):
    print("BAZ")
elif ((number % 3) == 0):
    print("BIZ")
elif ((number % 3 and number % 2) == 0):
    print("ZIZI")