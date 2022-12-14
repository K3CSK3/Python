start :int = None
end :int = None
osszeg :int = 0
elsoSzam :int = 0
masodikSzam :int = 0
elso :bool = True

print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
start = int(input())
print("Adja meg a végső értéket: ", end='')
end = int(input())


for i in range(end, start+1, 1):
    if elso:
        osszeg += i
        elso = False
    else:
        osszeg -= i
        elso = True
print(osszeg)