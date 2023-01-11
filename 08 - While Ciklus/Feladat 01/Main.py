szam :int = None

print("Adjon meg egy számot 0 és 9 között: ",end="")
szam = int(input())
while (szam < 0 or szam > 9):
    print("Adjon meg egy számot 0 és 9 között: ",end="")
    szam = int(input())