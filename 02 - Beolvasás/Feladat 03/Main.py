from os import system

name : str = None
height : int = None

name = str(input("\nAdja meg a nevét "))
height = float(input("Adja meg a magasságát(m) "))

system('cls')

print(f"{name} az ön magassága {height}m!\n")