szam :int = None
osszeg :int = 0
print("Adjon meg egy számot: ",end="")
szam = int(input())
while (osszeg < 100):
    print("Adjon meg egy számot: ",end="")
    szam = int(input())
    osszeg += szam
    print(osszeg)