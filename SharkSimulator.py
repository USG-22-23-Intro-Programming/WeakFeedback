

from graphics import *
from Button import *
import random
from FishClass import *
from shark import *



def main():

    grid()

#AQUATICS
    F1 = fish(win)
    F2 = fish(win)
    F3 = fish(win)
    S = shark(win)
#FISHES in a list
    fishsss = [F1, F2, F3]

#BUTTONS
    Q = Button(win, Point(500, 500), Point(550, 540), "plum1", "QUIT")
    R = Button(win, Point(500, 450), Point(550, 490), "plum1", "Reset")
    M = Button(win, Point(500, 400), Point(550, 440), "plum1", "Move")
    Square = Polygon(Point(shark[0] - 120,shark[1] - 120), Point(shark[0] + 120, shark[1] - 120), Point (shark[0] + 120, shark[1] + 120), Point(shark[0] - 120, shark[1] + 120))
    Square.draw(win)
    while True:

        m = win.getMouse()

        if R.isClicked(m):

            S.undraw()
            for fishes in fishsss:
                fishes.undraw() #undraws every fish?
            main()

        if M.isClicked(m):
            for fishes in fishsss:
                fishes.undraw()
                fishes.randomMove(win)






'''def main():
    
    grid()

#AQUATICS
    F1 = fish(win)
    F2 = fish(win)
    F3 = fish(win)
    S = shark(win)
#FISHES in a list
    fishsss = [F1, F2, F3]

#BUTTONS
    Q = Button(win, Point(500, 500), Point(550, 540), "plum1", "QUIT")
    R = Button(win, Point(500, 450), Point(550, 490), "plum1", "Reset")
    M = Button(win, Point(500, 400), Point(550, 440), "plum1", "Move")
    

    while True:
        
        m = win.getMouse()

        if R.isClicked(m):

            S.undraw()
            for fishes in fishsss:
                fishes.undraw() #undraws every fish?
            main()
            
        if M.isClicked(m):
            for fishes in fishsss:
                fishes.undraw()
                fishes.randomMove(win)
            #femke and winnie did this over facetime
            #fish one 
            if (loc4[0] - loc1[0]) < (loc4[1] - loc1[1]):

                #l/r
                if loc4[0] > loc1[0]:
                    if loc1[0] == 50:
                        loc1 = rightFish
                    else:
                        loc1 = leftFish

                else:
                    if loc1[0] == 430:
                        loc1 = leftFish
                    else:
                        loc1 = rightFish

            else:
                #up/down
                if loc4[1] < loc1[1]:
                    if loc1[1] == 430:
                        loc1 = downFish
                    else:
                        loc1 = upFish

                else:
                    if loc1[1] == 50:
                        loc1 = upFish
                    else:
                        loc1 = downFish

            #fish 2
            if (loc4[0] - loc2[0]) < (loc4[1] - loc2[1]):
                
                #l/r
                if loc4[0] > loc2[0]:
                    if loc2[0] == 50:
                        loc2 = rightFish2
                    else:
                        loc2 = leftFish2
                else:
                    if loc2[0] == 430:
                        loc2 = leftFish2
                    else:
                        loc2 = rightFish2
 
            else:
                
                #up/down
                if loc4[1] < loc2[1]:
                    if loc2[1] == 430:
                        loc2 = downFish2
                    else:
                        loc2 = upFish2

                else:
                    if loc2[1] == 50:
                        loc2 = upFish2
                    else:
                        loc2 = downFish2

            #FISH 3
            if (loc4[0] - loc3[0]) < (loc4[1] - loc3[1]):

                #l/r
                if loc4[0] > loc3[0]:
                    if loc3[0] == 50:
                        loc3 = rightFish3
                    else:
                        loc3 = leftFish3
                else:
                    if loc3[0] == 430:
                        loc3 = leftFish3
                    else:
                        loc3 = rightFish3

            else:

                #up/down
                if loc4[1] < loc3[1]:
                    if loc3[1] == 430:
                        loc3 = downFish3
                    else:
                        loc3 = upFish3

                else:
                    if loc3[1] == 50:
                        loc3 = upFish3
                    else:
                        loc3 = downFish3
            

        if Q.isClicked(m):
            break

    win.close()'''
            
        

def grid():
    x = 0
    y = 0

    #vertical lines
    for i in range(21):

        verticals = Line(Point(x, 0), Point(x, 400))
        verticals.draw(win)

        x = x + 20

    #horizontal lines
    for i in range(21):

        horizontals = Line(Point(0, y), Point(400, y))
        horizontals.draw(win)

        y = y + 20


if __name__ == "__main__":

    win = GraphWin("ooo big shark scary", 600, 600)
    win.setBackground("white")

    main()

