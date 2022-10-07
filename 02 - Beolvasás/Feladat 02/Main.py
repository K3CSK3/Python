from os import system

name :str = None
yearOfBirth :int = None

name = input("\nAdja meg a nevét: ")
yearOfBirth = int(input("Adja meg a születési évét "))

system('cls')

print(f"{name} ön {yearOfBirth} született!\n")