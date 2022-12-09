start :int = None
end :int = None
print("--------------------------")
print("Adja meg a kezdő értéket: ", end='')
start = int(input())
print("Adja meg a végső értéket: ", end='')
end = int(input())

if (start < end):
    for i in range(start, end+1, 1):
        if (i % 2):
            print(i)
else: 
    for i in range(end, start+1, 1):
        if (i % 2):
            print(i)