from os import system

resistance1 :int = None
resistance1 :int = None
connectionType :str = None

print("Adja meg az egyik ellenállás erejét: ",end='')
resistance1 = int(input())
print("Adja meg a másik ellenállás erejét: ",end='')
resistance2 = int(input())
print("Adja meg a kötés típusát: ",end='')
connectionType = input()

system('cls')

match connectionType:
    case "p":
        print((resistance1+resistance2)/(resistance1*resistance2))
    case "P":
        print((resistance1+resistance2)/(resistance1*resistance2))
    case "s":
        print(resistance1+resistance2)
    case "S":
        print(resistance1+resistance2)