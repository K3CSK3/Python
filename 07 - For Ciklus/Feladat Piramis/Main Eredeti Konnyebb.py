print("Kérem adja meg hány elemű a számpiramis?")
szam = int(input())
for i in range(0, szam):
    for j in range(0, i+1):
        print(f"{szam} ", end="")
print()


n = int(input("Enter the number of rows")) 
for i in range(0, n): 
    for j in range(0, i + 1): 
        print(f"{n} ", end="") 
    print() 