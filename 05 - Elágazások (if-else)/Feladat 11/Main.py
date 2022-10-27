from os import system

number :int = None

print("Adjon meg egy számot: ",end='')
number = int(input())

system('cls')

if (number > 0 and (number % 2) == 0 and (number % 5) == 0):
    print("A szám pozitív, páros és osztható öttel")
elif (number > 0 and (number % 2) == 0 and number % 5):
    print("A szám pozitív, páros de nem osztható öttel")
elif (number > 0 and number % 2 and (number % 5) == 0):
    print("A szám pozitív, osztható öttel de nem páros")

elif (number < 0 and (number % 2) == 0 and (number % 5) == 0):
    print("A szám negatív, páros és osztható öttel")
elif (number < 0 and (number % 2) == 0 and number % 5):
    print("A szám negatív, páros de nem osztható öttel")
elif (number < 0 and number % 2 and (number % 5) == 0):
    print("A szám negatív, osztható öttel de nem páros")