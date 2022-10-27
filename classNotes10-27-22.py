#lists are like strings that they hold a collection of elements in a specific order.
#Instead of quotation marks/ parentheses they use brackets
names = ["Lyzane", "Zuri", "Trinity", "Olumat", "Eisha", "Nawal", "Jaein"]
#access first element by:    
print(names[0])
#access last element by:
print(names[-1])
#print last element:
print("Last element: ")
print(names[len(names)-1])
#names.append adds name to end of list
names.append("Serena")
#remove certain element once from list
names.remove("Jaein")

for i in range(len(names)):
#repeats the amount of elements in list
    print(names[i])
#another way (for each loop)(for each/name in list/names):
for name in names:
    print(name)

fames = ["Zuri", "Considine", "Hamilton", "Lafayette", "Galileo", "Aristotle"]

for i in range(len(names)):
    print(names[i])

for name in fames:
    if name == "Considine":
        print("Mr.Considine, here")
    else:
       print("Hello, famous" + name) 
#get index (position) of an element in a list)
print(names.index("Galileo"))
print(names.index("Zuri"))

def main():
     
    #lists are like strings that they hold a collection of elements in a specific order.
    #Instead of quotation marks/ parentheses they use brackets
    names = ["Lyzane", "Zuri", "Trinity", "Olumat", "Eisha", "Nawal", "Jaein"]
    #access first element by:    
    print(names[0])
    #access last element by:
    print(names[-1])
    #print last element:
    print("Last element: ")
    print(names[len(names)]-1)
    #names.append adds name to end of list
    names.append("Serena")
    #remove certain element once from list
    names.remove("Jaein")

    for i in range(len(names)):
    #repeats the amount of elements in list
        print(names[i])
    #another way (for each loop)(for each/name in list/names):
    for name in names:
        print(name)

    fames = ["Zuri", "Considine", "Hamilton", "Lafayette", "Galileo", "Aristotle"]

    for i in range(len(names)):
        print(names[i])

    for name in fames:
        if name == "Considine":
            print("Mr.Considine, here")
        else:
           print("Hello, famous" + name)
    #get index (position) of an element in a list)
    print(names.index("Galileo"))
    print(names.index("Zuri"))









    z = zoo()
    animal = "leopard"
    print("The " + animal + " lives in the  " + Z.getHabitat(animal))
    habitat = "wetlands"
    print("In the " + "there is a " + Z.getanimal(habitat))

          
def __init__(self):
    self.animals = ["Tiger", "Bear", "Fish"]
    self.habitats = ["Jungle", "Forest", "Sea"]




if __name__ == "__main__":
    main()
