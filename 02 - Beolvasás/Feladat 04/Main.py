from xml.dom.minidom import NamedNodeMap


name :str = None
pressedKey :str = None

name = input("\nAdja meg a nevét: ")
pressedKey = input("Üssön le egy billentyűt ")

print(f"{name} ön a/az {pressedKey} billentyűt nyomta meg!")