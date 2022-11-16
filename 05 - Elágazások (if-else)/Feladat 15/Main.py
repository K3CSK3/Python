from os import system

eloetel :int = None
eloetelszoveg :str = None
zoldsegleves :bool = False
husleves :bool = False
gyumolcsleves :bool = False

foetel :int = None
foetelszoveg :str = None
sultCsirkecomb :bool = False
sultCsirkemell :bool = False
rakottzoldseg :bool = False
spagetti :bool = False
pizza :bool = False

koret :int = None
koretszoveg :str = None
rizs :bool = False
paroltzoldseg :bool = False
gyumolcs :bool = False
sultkrumpli :bool = False
salata :bool = False
kola :bool = False

ertekeles :str = None

print("Előétel\n1-Zöldségleves\n2-Húsleves\n3-Gyümölcsleves\nMit választ: ",end='')
eloetel = int(input())
if eloetel == 1:
    zoldsegleves = True
    eloetelszoveg = "Zöldségleves"
elif eloetel == 2:
    husleves = True
    eloetelszoveg = "Húsleves"
elif eloetel == 3: 
    gyumolcsleves = True
    eloetelszoveg = "Gyümölcsleves"
else:
    print("Nincs ilyen opció")
    eloetelszoveg = "Semmi"

print("Főétel:\n1-Sültcsirkecomb\n2-Sült csirkemell\n3-Rakottzöldség\n4-Spagetti\n5-Pizza\nMit választ: ",end='')
foetel = int(input())
if foetel == 1:
    sultCsirkecomb = True
    foetelszoveg = "Sültcsirkecomb"
elif foetel == 2:
    sultCsirkemell = True
    foetelszoveg = "Sült csirkemell"
elif foetel == 3: 
    rakottzoldseg = True
    foetelszoveg = "Rakottzöldség"
elif foetel == 4: 
    spagetti = True
    foetelszoveg = "Spagetti"
elif foetel == 5: 
    pizza = True
    foetelszoveg = "Pizza"
else:
    print("Nincs ilyen opció")
    foetelszoveg = "Semmi"

print("Köret:\n1-Rizs\n2-Pároltzöldség\n3-Gyümölcs\n4-Sültkrumpli\n5-Saláta\n6-Kóla\nMit választ: ",end='')
koret = int(input())
if koret == 1:
    rizs = True
    koretszoveg = "Rizs"
elif koret == 2:
    paroltzoldseg = True
    koretszoveg = "Pároltzöldség"
elif koret == 3: 
    gyumolcs = True
    koretszoveg = "Gyümölcs"
elif koret == 4: 
    sultkrumpli = True
    koretszoveg = "Sültkrumpli"
elif koret == 5: 
    salata = True
    koretszoveg = "Saláta"
elif koret == 6: 
    kola = True
    koretszoveg = "Kóla"
else:
    print("Nincs ilyen opció")
    koretszoveg = "Semmi"

system('cls')

if ((eloetel == 1) and (foetel == 4) and ((koret == 3) or (koret == 5))):
    ertekeles = "Kiváló"


print(f"A mai menü értékelése: {ertekeles}")
print(f"A mai menü tartalma: {eloetelszoveg}, {foetelszoveg}, {koretszoveg}")
