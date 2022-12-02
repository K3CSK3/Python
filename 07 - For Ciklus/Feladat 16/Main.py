start :int = None
end :int = None
print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
start = int(input())
print("Adja meg a végső értéket: ", end='')
end = int(input())

if (start > end):
    osszeg = 0
    osszeg2 = 0
    mennyiseg = 1
    for i in range(start, end-1, -1):
        if (i % 2 == 0):
            osszeg += i
        else:
            osszeg2 += i
    mennyiseg += 1
    print((osszeg+osszeg2)/mennyiseg)

else: 
    osszeg = 0
    osszeg2 = 0
    mennyiseg = 1
    for i in range(end, start-1, -1):
        if (i % 2 == 0):
            osszeg += i
        else:
            osszeg2 += i
    mennyiseg += 1
    print((osszeg+osszeg2)/mennyiseg)
