start :int = None
end :int = None
print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
start = int(input())
print("Adja meg a végső értéket: ", end='')
end = int(input())

if (start > end):
    osszeg = 0
    osszeg2 = 1
    for i in range(start, end-1, -1):
        if (i % 2 == 0):
            osszeg += i
        elif (i % 2):
            osszeg2 = osszeg2 * i
    print(f" Az Összegük: {osszeg}\n A szorzatuk: {osszeg2}")
else: 
    osszeg = 0
    osszeg2 = 1
    for i in range(end, start-1, -1):
        if (i % 2 == 0):
            osszeg += i
        elif (i % 2):
            osszeg2 = osszeg2 * i
    print(f" A páros számok összege: {osszeg}\n A páratlan számok szorzata: {osszeg2}")