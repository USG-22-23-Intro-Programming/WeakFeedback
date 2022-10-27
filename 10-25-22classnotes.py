#class definition

    #in order to create a class/sprite you use the owrd class and give it a name

'''class Person:
    def __init__(self, age, name): #called constructor method--> builds object
        self.hairColor = "black"
        self.age = 35
        self.name = name

    def getAge(self):
        return self.age
    def getName(self):
        return self.name
    def drinkWater(self, volume):
        print("Wow I just drank " + str(volume) + " liters of water")

#main method

def main():
    Lyzane = Person(15, "Lyzane")

    mrC = Person(75, "Considine")

    Jaewon = Person(15, "J-Money")
    
    print(Lyzane.getName() + " is " + str(Lyzane.getAge()) + " years old")
    print(Jaewon.getName() + " is " + str(Jaewon.getAge()) + " years old")
    print(mrC.getName() + " is " + str(mrC.getAge()) + " years old")

    mrC.drinkWater(2)
    myS = "hello world"

    char = myS[7]
    print(char)#finds character

#index can also take in a starting position and ending position
    ind = myS.index("lo")
    print(ind) #finds string number
    
    ind2 = myS.index("o", 5, 9)
    print(ind2)

    count = myS.count("o")
    print(count)

    count = myS.count("z")
    print(count)

    newString = "      This example was scuffed     "
    newString = newString.strip()
    print(newString)

    newString2 = "       !aabbMr. ConsidineqqmM  "
    newString2 =newString2.strip(" !abqmM")
    print(newString2)

    print(newString2.replace("ons", ""))
 #for loop: repeat something a specific amount of times

    for i in range(5):
        print("hello")
        print(i)
    for i in range (10, 20):
        print("yellow")
        print(i)
    name = "Annie Wright"
    for i in range(10):
        print(name[i])

    for i in range(len(name)):
        print(name[i])

    answer = "I don't know"
    for char in answer:
        print(char)

    y = 50
    while(y > 10):
        print("this value: " + str(y))
        y = y - 2
    
    while True:
        print("never leave class")
        break

    String = "never leave class"
    i = 0
    while True:
        print(String)
        check = String[i]
        if check == "c":
            break
        else:
            i = i+1
            
#we can use it to access different characters of Annie Wright
#i keep track of certain number of repitition
    
if __name__ == "__main__":
    main()

#method have parentheses at the end of the method while variable don't (parentheses is where the parameter goes)
#string methods
    -index
    -count
    -capitalize
    -strip "gets rid of white space" (removes white space that is leading or trailing string)
    -replace "replaces all instences" '''

#hw

#x = (int(input("put in a number! ")))
#factorial(x)'''






def factorial(x):
    y = 1
    for i in range(1, x+1):
       y = y * i

       
    print("The factorial is: " + str(y))
    



def doubleIt():

    phrase = input("Enter a phrase to double")
    s = " "

    for i in phrase:
        s = s + i + i
     
    print(s)


def camelCode():
    phrase2 = input("Please enter a file name")
    pop = phrase2.replace("/", "-")
    v = pop.title()
    e = v.replace(" ", "")
    f = e[0]
    d = f.lower()
    r = e.replace(f, d)
    print(r)
    
    
def main():
   factorial(9)
   doubleIt()
   camelCode()
 

if __name__ == "__main__":
    main()  








        
