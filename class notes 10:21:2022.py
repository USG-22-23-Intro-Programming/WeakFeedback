#w3schools=website that has info on coding

#x=5   means: set x equal to five
#x == 5 means: is x equal to five?
def isMultiple(num1,num2):
    x = num1 % num2
    if x == 0:
        print(str(num1) + " is a multiple of " + (str(num2))
    else:
        print(str(num1) + " it is not a multiple" + (str(num2))
        
def main():
    isMultiple(5,2)

    answer = palindrome()
    print(answer)
    
if __name__ == "__main__":
    main()

#allows main method to be called

def palindrome
    s = input("Type in a palindrome you want to test")
    length= len(s)
    for i in range(length):
        if s[i] != s[length - 1 - i]
            return False
    return True
# s[first] == s[last]
# len()= find length of()
# if s = hello, len(s) == 5, s[0] == s[len(s)-1]
# count = 0
#for loop: repeat
# i: iterator (starts at 0)(adds one each time)
#brackets are used for indexes or positions
# parentheses are used for methods
#!= means: not equal
#if our first character is not equal to out last character
#return is output of a method
# "" is empty string
