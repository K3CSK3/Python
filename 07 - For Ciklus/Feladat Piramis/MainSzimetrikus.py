sor :int = 0
lista :list = []

print("Kérem adja meg hány elemű a számpiramis?")
sor = int(input())
for i in range(0, sor+1, 2):
    print(' '.join(map(str, lista)))
    lista.append(f"  {i+1}  ")
    lista.append(f"  {i+2}  ")