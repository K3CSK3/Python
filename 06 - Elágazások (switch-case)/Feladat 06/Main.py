from os import system
from math import sqrt

oldal1 :int = None
oldal2 :int = None
connectionType :str = None

print("Adja meg az egyik oldal hosszát: ",end='')
oldal1 = int(input())
print("Adja meg a másik oldal hosszát: ",end='')
oldal2 = int(input())
print("Adja meg a művelet típusát(terület, kerület, átló): ",end='')
connectionType = input()

system('cls')

match connectionType:
    case "t":
        print(f"A téglalap területe: {oldal1 * oldal2}")
    case "k":
        print(f"A téglalap kerülete: {(oldal1 + oldal2) * 2}")
    case "á":
        print(f"A téglalap átlója{sqrt((oldal1 * oldal1) + (oldal2 * oldal2))}")
    case _:
        print("Nincs ilyen művelet")