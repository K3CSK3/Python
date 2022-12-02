start :int = None
end :int = None
print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
start = int(input())
print("Adja meg a végső értéket: ", end='')
end = int(input())

if (start > end):
    osszeg = 0
    for i in range(end, start-1, -1):
        if (i % 3 == 0):
            osszeg += 1
    print(f"{osszeg} szám osztható 3-al")
else: 
    osszeg = 0
    for i in range(end, start-1, -1):
        if (i % 3 == 0):
            osszeg += 1
    print(f"{osszeg} szám osztható 3-al")