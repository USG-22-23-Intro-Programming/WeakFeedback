from graphics import*
from Button import*

def main():
    win = GraphWin("Palindrome", 800, 600) #measure of dimensions of window which is in pixels

    Q = Button(win, Point(600,500), Point(700,575), "tomato", "QUIT")
    Check = Button(win, Point(350, 350),Point(450, 425), "SteelBlue1", "Check!")
    
    E = Entry(Point(400, 300), 30)
    E.draw(win)
    E.setSize(16)
    T = Text(Point(400, 250), "Write a potential Palindrome below!")
    T.draw(win)
    Tru = Text(Point(400, 500), "Yes, it is a palindrome!")
    Fal = Text(Point(400, 500), "No, it is not a palindrome!")
    while True:
        m = win.getMouse()
        if Q.isClicked(m):
            break
        if Check.isClicked(m):
            
            palindrome = True
            pal = E.getText()
            length = len(pal)
            for i in range(len(pal)):
                if pal[i] != pal[length - 1 - i]:
                    palindrome = False   
                
                    
            if palindrome == False:
                Fal.undraw()
                Tru.undraw()
                Fal.draw(win)
            if palindrome == True:
                Fal.undraw()
                Tru.undraw()
                Tru.draw(win)
                


#:

    ''' s = input("Type in a palindrome you want to test")
    length= len(s)
    for i in range(length):
        if s[i] != s[length - 1 - i]
            return False
    return True'''
    win.close()
    

if __name__ == "__main__":
    main()
