from os import system

resistance1 :int = None
resistance1 :int = None
connectionType :str = None

print("Adja meg az egyik ellenállás értékét: ",end='')
resistance1 = int(input())
print("Adja meg a másik ellenállás értékét: ",end='')
resistance2 = int(input())
print("Adja meg a kötés típusát: ",end='')
connectionType = input()

system('cls')

match connectionType:
    case ["p","P"]:
        print((resistance1+resistance2)/(resistance1*resistance2))
    case ["s","S"]:
        print(resistance1+resistance2)