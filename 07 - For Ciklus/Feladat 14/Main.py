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
    for i in range(end, start-1, -1):
        if (i % 5 == 0):
            osszeg += i
        elif (i % 7 == 0):
            osszeg2 += i
    if osszeg > osszeg2:
        print(f"Az öttel osztható számok összege a nagyobb")
    else:
        print(f"A héttel osztható számok összege a nagyobb")

else: 
    osszeg = 0
    osszeg2 = 0
    for i in range(start, end-1, -1):
        if (i % 5 == 0):
            osszeg += i
        elif (i % 7 == 0):
            osszeg2 += i
    if osszeg > osszeg2:
        print(f"Az öttel osztható számok összege a nagyobb")
    else:
        print(f"A héttel osztható számok összege a nagyobb")
